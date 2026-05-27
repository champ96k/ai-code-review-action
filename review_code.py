import os
import requests
import google.generativeai as genai
from google.api_core import exceptions

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
REPO = os.getenv("GITHUB_REPOSITORY")
PR_NUMBER = os.getenv("GITHUB_EVENT_NUMBER")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_pr_changes():
    url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}/files"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print("❌ Failed to fetch PR files:", response.text)
        exit(1)
    return response.json()

def format_review_prompt(pr_files):
    code_reviews = []
    for file in pr_files:
        if "patch" in file:
            filename = file["filename"]
            patch = file["patch"]
            code_reviews.append(f"File: {filename}\nChanges:\n{patch}")
    return "\n\n".join(code_reviews)

def build_prompt(code_review_text):
    return f"""
You are a **senior software engineer** reviewing a GitHub pull request.

### Guidelines:
- ✅ Approve if no major issues. Respond with **"LGTM"**.
- 🔍 Flag only clear bugs/security/performance issues.
- ✨ Minor suggestions are optional.
- 🚫 Avoid stylistic or subjective changes.
- 🔥 Keep it concise.

Now review this code:

{code_review_text}

Respond in **Markdown format**.
"""

def run_gemini(prompt):
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel("models/gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") else None
    except Exception as e:
        print("⚠️ Gemini error:", str(e))
        return None

def run_openrouter(prompt):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mixtral-8x7b",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            },
            timeout=30
        )
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("⚠️ OpenRouter error:", str(e))
        return "⚠️ AI Review Failed: Could not generate a response using Gemini or OpenRouter."

def post_comment(body):
    url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
    response = requests.post(url, headers=HEADERS, json={"body": body})
    if response.status_code == 201:
        print("✅ Review posted successfully!")
    else:
        print("❌ Failed to post review:", response.text)
        exit(1)

# Main Logic
pr_files = fetch_pr_changes()
if not pr_files:
    print("No code changes found.")
    exit(0)

prompt = build_prompt(format_review_prompt(pr_files))
review_text = run_gemini(prompt) or run_openrouter(prompt)

if review_text.lower() in ["lgtm", "lgtm!", "looks good"]:
    review_text = "✅ LGTM! No major issues found. Good to go! 🚀"

post_comment(review_text)
