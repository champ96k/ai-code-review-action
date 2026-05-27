#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored messages
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Check if description is provided
if [ -z "$1" ]; then
    print_error "Please provide a release description"
    echo "Usage: ./publish.sh 'Your release description'"
    exit 1
fi

RELEASE_DESCRIPTION="$1"

# Get current version from latest tag
CURRENT_VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
print_message "Current version: $CURRENT_VERSION"

# Extract version numbers
VERSION_PARTS=(${CURRENT_VERSION//./ })
MAJOR=${VERSION_PARTS[0]#v}
MINOR=${VERSION_PARTS[1]}
PATCH=${VERSION_PARTS[2]}

# Increment patch version
NEW_PATCH=$((PATCH + 1))
NEW_VERSION="v$MAJOR.$MINOR.$NEW_PATCH"

print_message "New version will be: $NEW_VERSION"

# Update version in action.yml
sed -i '' "s/version: .*/version: $NEW_VERSION/" action.yml
print_message "Updated version in action.yml"

# Create new tag
print_message "Creating new tag: $NEW_VERSION"
git tag -a "$NEW_VERSION" -m "$RELEASE_DESCRIPTION"

# Push changes and tag
print_message "Pushing changes to GitHub..."
git push origin main
git push origin "$NEW_VERSION"

# Create GitHub release using GitHub CLI
if command -v gh &> /dev/null; then
    print_message "Creating GitHub release..."
    gh release create "$NEW_VERSION" \
        --title "Release $NEW_VERSION" \
        --notes "$RELEASE_DESCRIPTION"
else
    print_warning "GitHub CLI not found. Please create release manually at:"
    echo "https://github.com/champ96k/ai-code-review-action/releases/new"
fi

print_message "Release process completed!"
print_message "New version: $NEW_VERSION"
print_message "Description: $RELEASE_DESCRIPTION" 