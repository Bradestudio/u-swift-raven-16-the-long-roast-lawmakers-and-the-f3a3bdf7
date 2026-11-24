# SPDX-License-Identifier: MIT
# make.fun bounty: u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7
# "The Long Roast: Lawmakers and the File They Cannot Convert"
#
# Writes one single satirical sentence to /output/entry.txt, roasting
# lawmakers who would regulate AI, crypto or the internet but cannot
# convert a file to PDF.
#
# Draft 1 of the line. The setup grants Congress full authority over
# the entire internet, then the turn undercuts it with one specific,
# unglamorous habit: the senator who writes the law still prints his
# Word file, scans it back in, and calls the result a PDF. The
# print-and-scan loop is a concrete, unexpected detail — not the worn
# "can't use email" cliche — and the punch lands on the last few words.
#
# Revision 1: "calls the result a PDF" became "proudly calls the result
# a PDF". The extra word paints the oblivious pride that makes the
# undercut land: he does not merely fail to convert the file, he is
# satisfied with the print-and-scan workaround and believes it IS the
# PDF. One word, same turn, sharper punch on the last few words.
#
# The competition gate is 1-320 characters, so it is enforced here, in
# code: length is counted in Unicode code points, and a blank-only or
# multi-line text is rejected, so a future edit that makes the text too
# long (or empty) fails loudly instead of producing an invalid entry.
# The file is written atomically (temp file + rename) so
# /output/entry.txt is never left half-written. No trailing newline:
# the gate counts characters, and the entry is the line itself, exactly
# as written. Stdlib only, no network.
import os

# Final entry (one line):
# "Congress can pass a law to regulate the entire internet, but the
# senator writing it still prints his Word file, scans it back in,
# and proudly calls the result a PDF."
ENTRY = (
    "Congress can pass a law to regulate the entire internet, but the "
    "senator writing it still prints his Word file, scans it back in, "
    "and proudly calls the result a PDF."
)


def validate_entry(text: str) -> int:
    """Enforce the competition gate: 1-320 code points, single line."""
    length = len(text)
    if length < 1 or length > 320:
        raise ValueError(
            f"entry length {length} code points is outside the 1-320 range"
        )
    if text.strip() == "":
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for ch in text:
        code = ord(ch)
        if code < 0x20 and ch != "\t":
            raise ValueError(f"entry contains a control character U+{code:04x}")
    return length


def main() -> None:
    entry_length = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    # Revision 2: verify the write round-trips byte-for-byte, so what
    # the judge reads is exactly the validated string above — no stray
    # newline, no encoding surprise. The gate counts characters, but
    # the tie-break counts bytes, so both numbers are reported.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError(
            "round-trip mismatch: /output/entry.txt differs from the "
            "validated entry"
        )
    print(
        f"wrote {entry_length} code points "
        f"({len(ENTRY.encode('utf-8'))} bytes) to /output/entry.txt"
    )


if __name__ == "__main__":
    main()
