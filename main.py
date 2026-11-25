"""One Star, Written in Sap.

Writes a single one-line 1-star review from a houseplant about the
human who owns it to /output/entry.txt.

The line is written in the plant's own voice: a fern bought for its
"low-maintenance" label, overwatered like a goldfish, parked by a
window that barely sees the sun, and unimpressed enough to call the
arrangement a timeshare.
"""

import os

ENTRY = (
    "One star. Bought me because the tag said 'low-maintenance', "
    "then watered me like a goldfish and parked me by a window that "
    "gets eleven minutes of sun a day. I am a fern, not a timeshare."
)


def main():
    # The gate allows 1 to 279 characters; refuse to emit an entry
    # that would fail it rather than submitting an invalid line.
    if not 1 <= len(ENTRY) <= 279:
        raise ValueError("entry must be 1-279 characters, got %d" % len(ENTRY))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
