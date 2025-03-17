#!/bin/bash

set -e

TAG=$(python -c 'from my_project.version import __version__; print("v" + __version__)')

read -p "Creating new release for $TAG. Do you want to continue? [Y/n] " prompt

if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]; then
    # Create a release branch
    RELEASE_BRANCH="release/$TAG"
    git checkout -b "$RELEASE_BRANCH"

    # Stage and commit changes
    git add -A
    git commit -m "Bump version to $TAG for release"

    # Push the release branch
    git push -u origin "$RELEASE_BRANCH"

    # Create pull request message
    echo "릴리스 준비가 완료되었습니다. 다음 단계를 진행해주세요:"
    echo "1. $RELEASE_BRANCH 브랜치에서 main으로 Pull Request를 생성해주세요"
    echo "2. Pull Request가 머지되면, 나머지 release 작업은 자동으로 진행됩니다."
else
    echo "취소되었습니다"
    exit 1
fi
