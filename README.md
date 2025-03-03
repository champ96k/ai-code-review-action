# AI Code Review GitHub Action

🚀 This GitHub Action uses Google Gemini AI to review PRs and provide feedback.

## Usage

Add this to your `.github/workflows/ai_review.yml`:

```yaml
name: AI Code Review
on: pull_request
jobs:
  ai_review:
    runs-on: ubuntu-latest
    steps:
      - name: Run AI Code Review
        uses: your-username/ai-code-review-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          google_api_key: ${{ secrets.GOOGLE_API_KEY }}
```
