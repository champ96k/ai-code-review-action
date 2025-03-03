import os
import requests
import google.generativeai as genai

# Read input variables from GitHub Action
GITHUB_TOKEN = os.getenv("INPUT_GITHUB_TOKEN")
GOOGLE_API_KEY = os.getenv("INPUT_GOOGLE_API_KEY")
REPO = os.getenv("GITHUB_REPOSITORY")
PR_NUMBER = os.getenv("GITHUB_EVENT_NUMBER")

# Configure Google Gemini AI
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-pro-exp")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Fetch PR changes
pr_files_url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}/files"
response = requests.get(pr_files_url, headers=HEADERS)
if response.status_code != 200:
    print("❌ Failed to fetch PR files:", response.text)
    exit(1)

pr_files = response.json()
if not pr_files:
    print("No code changes found to review.")
    exit(0)

# Prepare AI Review
code_reviews = [f"File: {f['filename']}\nChanges:\n{f['patch']}" for f in pr_files if "patch" in f]
code_review_text = "\n\n".join(code_reviews)

# AI Prompt
prompt = f"""
You are a senior engineer reviewing a GitHub PR.
If no major issues, reply "✅ LGTM!". Otherwise, suggest fixes.

{code_review_text}
"""

response = model.generate_content(prompt)
review_comments = response.text.strip() if response and hasattr(response, "text") else "❌ AI error."

# Post Review Comment
review_url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
requests.post(review_url, headers=HEADERS, json={"body": review_comments})

print("✅ Review posted successfully!")
