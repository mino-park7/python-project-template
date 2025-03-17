"""Prepares markdown release notes for GitHub releases."""

import os
from typing import Optional

import packaging.version

TAG = os.environ["TAG"]


def get_commit_history() -> str:
    """Get the commit history for the given tag.

    Returns:
        str: The commit history for the given tag.
    """
    new_version = packaging.version.parse(TAG)

    # Pull all tags.
    os.popen("git fetch --tags")

    # Get all tags sorted by version, latest first.
    all_tags = os.popen("git tag -l --sort=-version:refname 'v*'").read().split("\n")

    # Out of `all_tags`, find the latest previous version so that we can collect all
    # commits between that version and the new version we're about to publish.
    # Note that we ignore pre-releases unless the new version is also a pre-release.
    last_tag: Optional[str] = None  # noqa: FA100
    for tag in all_tags:
        if not tag.strip():  # could be blank line
            continue
        try:
            version = packaging.version.parse(tag)
        except packaging.version.InvalidVersion:
            continue
        if new_version.pre is None and version.pre is not None:
            continue
        if version < new_version:
            last_tag = tag
            break
    if last_tag is not None:
        commits = os.popen(f"git log {last_tag}..{TAG} --oneline --first-parent").read()
    else:
        commits = os.popen("git log --oneline --first-parent").read()
    return "## Commits\n\n" + commits


def main():
    """Main function to generate release notes."""
    print(get_commit_history())  # noqa: T201


if __name__ == "__main__":
    main()
