# AI Code Review GitHub Action

A GitHub Action that automatically reviews pull requests using Google's Gemini AI. This action analyzes code changes and provides intelligent feedback directly on your pull requests.

## Features

- 🤖 Automated code review using Google's Gemini AI
- 📝 Detailed feedback on code changes
- 🔄 Runs automatically on pull requests
- 🎯 Configurable to run on specific branches
- 🔒 Secure handling of API keys
- 🛠️ Improved workspace handling
- 📦 Optimized Docker configuration

## Usage

### Basic Setup

Create a new file `.github/workflows/ai_review.yml` in your repository:

```yaml
name: Champ AI Code Review
on:
  pull_request:
    types: [opened, synchronize, reopened]
    branches:
      - master  # Only run on PRs targeting master branch

permissions:
  contents: read
  pull-requests: write

jobs:
  ai_review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Run AI Code Review
        uses: champ96k/ai-code-review-action@v1.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          google_api_key: ${{ secrets.GOOGLE_API_KEY }}
```

### Required Secrets

1. `GITHUB_TOKEN`: Automatically provided by GitHub Actions
2. `GOOGLE_API_KEY`: Your Google Gemini API key
   - Get it from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Add it in your repository settings under Settings → Secrets and variables → Actions

### Configuration Options

The action accepts the following inputs:

| Input | Required | Description |
|-------|----------|-------------|
| `github_token` | Yes | GitHub token for accessing PR details |
| `google_api_key` | Yes | Google Gemini API key for AI analysis |

## How It Works

1. When a pull request is created or updated, the action automatically triggers
2. It fetches the code changes from the PR
3. Sends the changes to Google's Gemini AI for analysis
4. Posts the AI's review as a comment on the PR

## Example Output

The action will post a comment on your PR that looks like this:

```
✅ LGTM!
```

Or if there are issues:

```
Here are some suggestions for improvement:

1. Consider adding error handling in the data processing function
2. The variable naming could be more descriptive
3. Missing documentation for the new API endpoint
```

## Version History

### v1.2 (Latest)
- 🐛 Fixed workspace path issues in Docker configuration
- 🔧 Improved argument handling for better reliability
- 📦 Updated Docker setup for better performance
- 🛠️ Enhanced error handling and logging

### v1.1
- ✨ Added support for multiple file reviews
- 🔍 Improved code analysis accuracy
- 📝 Enhanced review comment formatting

### v1.0
- 🚀 Initial release
- 🤖 Basic AI code review functionality
- 🔒 Secure API key handling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/champ96k/ai-code-review-action/issues) on GitHub.

## Latest Updates

The latest version (v1.2) includes several improvements:
- Fixed workspace path issues that were causing file not found errors
- Improved Docker configuration for better reliability
- Enhanced error handling and logging
- Optimized performance with better workspace management

To use the latest version, make sure to specify `@v1.2` in your workflow file:
```yaml
uses: champ96k/ai-code-review-action@v1.2
```
