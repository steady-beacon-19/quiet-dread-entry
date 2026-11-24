"""Two Days of Quiet Dread — entrypoint.

Writes one single-line code review comment (at most 140 characters) to
/output/entry.txt. The comment approves a pull request while carrying
quiet existential dread: flat tone, no melodrama, the laugh comes from
the dread itself.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The line: a plain approval a tired engineer would really paste, with
# the dread carried by one flat image \u2014 a stranger deleting the code
# without ever knowing who wrote it. No exclamation, no melodrama; the
# laugh comes from the dread itself, and it still ends as an approval.
COMMENT = (
    "Approving. Clean code, green tests, and one day a stranger will "
    "delete all of it without ever knowing our names. Ship it."
)


def main() -> None:
    text = COMMENT.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1..140 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
