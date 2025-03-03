AI Code Review GitHub Action<h1><strong>AI Code Review Action</strong> 🚀</h1>
<p><strong>AI-powered GitHub PR Code Reviewer using Google Gemini AI</strong></p>
<h2><strong>🔹 What It Does</strong></h2>
<p>This GitHub Action automatically reviews pull requests using <strong>Google Gemini AI</strong> and provides concise, actionable feedback on your code changes.</p>
<ul>
<li>✅ <strong>Approves PRs</strong> if no major issues are found.</li>
<li>🔍 <strong>Identifies bugs, security risks, and performance issues</strong>.</li>
<li>✨ <strong>Provides best practice suggestions</strong> (optional, non-blocking).</li>
<li>⏳ <strong>Avoids subjective or stylistic preferences</strong> for focused reviews.</li>
</ul>
<hr>
<h2><strong>⚙️ How It Works</strong></h2>
<ol>
<li>When a <strong>pull request is opened</strong>, this action fetches the code changes.</li>
<li>It sends the <strong>modified code</strong> to <strong>Google Gemini AI</strong> for review.</li>
<li>The AI generates feedback based on software engineering best practices.</li>
<li>The action <strong>posts a comment on the PR</strong> with the AI's review.</li>
</ol>
<hr>
<h2><strong>🛠 Setup &amp; Usage</strong></h2>
<p>To use this action in your GitHub repository, add the following workflow file:</p>
<pre><code class="language-yaml">name:Champ AI Code Review
on: pull_request
jobs:
  ai_review:
    runs-on: ubuntu-latest
    steps:
      - name: Run Champ AI Code Review
        uses: your-username/ai-code-review-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          google_api_key: ${{ secrets.GOOGLE_API_KEY }}
</code></pre>
<h3><strong>🔑 Required Inputs</strong></h3>

Name | Description | Required
-- | -- | --
github_token | GitHub Token for PR access | ✅ Yes
google_api_key | API Key for Google Gemini AI | ✅ Yes


<blockquote>
<p>📌 <strong>Note</strong>: Store these values securely as <strong>GitHub Secrets</strong> in your repository.</p>
</blockquote>
<hr>
<h2><strong>📝 Example PR Review Comment</strong></h2>
<p>When a developer submits a PR, the Champ AI Code Reviewer will respond like this:</p>
<pre><code>✅ LGTM! No major issues found. Good to go! 🚀
</code></pre>
<p>Or, if issues are detected:</p>
<pre><code>**File: `auth_service.dart`**
- **Issue:** Potential security risk with storing tokens in plaintext.
- **Why?** This could expose sensitive user data if compromised.
- **Suggested Fix:** Encrypt tokens before saving or use secure storage.

**File: `performance_helper.dart`**
- **Issue:** Looping through a large list multiple times.
- **Why?** This can impact performance in large-scale applications.
- **Suggested Fix:** Refactor using a single-pass algorithm.

---
🔍 *Make these changes for better security &amp; performance!*
</code></pre>
<hr>
<h2><strong>💡 Why Use This Action?</strong></h2>
<p>✅ <strong>Automates PR Reviews</strong> with AI-powered feedback.<br>
🕒 <strong>Saves Engineering Time</strong> by identifying key issues instantly.<br>
📈 <strong>Improves Code Quality</strong> with best practice recommendations.<br>
🔒 <strong>Enhances Security &amp; Performance</strong> in your repository.</p>
<hr>
<h2><strong>📌 Notes</strong></h2>
<ul>
<li>Requires a <strong>Google Gemini AI API key</strong>. Get it from <a href="https://aistudio.google.com/">Google AI Studio</a>.</li>
<li>Works with <strong>all programming languages</strong>.</li>
<li>Designed for <strong>concise, to-the-point feedback</strong>.</li>
</ul>
<hr>
