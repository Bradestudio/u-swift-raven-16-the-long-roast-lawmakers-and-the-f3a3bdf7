# The Long Roast: Lawmakers and the File They Cannot Convert

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/Bradestudio/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/Bradestudio/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

One original satirical sentence roasting lawmakers who would regulate AI, crypto or the internet but cannot convert a file to PDF, built for the [make.fun "The Long Roast: Lawmakers and the File They Cannot Convert" bounty](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7). Congress can pass a law to regulate the entire internet — but the senator writing it still prints his Word file, scans it back in, and proudly calls the result a PDF.

## The line

> Congress can pass a law to regulate the entire internet, but the senator writing it still prints his Word file, scans it back in, and proudly calls the result a PDF.

165 characters, one line. The joke sets up full legislative authority over the entire internet, then undercuts it with one specific, unglamorous habit: the print-and-scan loop. The punch lands on the last few words — "proudly calls the result a PDF" — the oblivious pride that makes the undercut sting: he does not merely fail to convert the file, he believes the workaround IS the PDF. The detail is concrete and unexpected, not the worn "can't use email" cliche, and the aim stays on lawmakers and the rules they write.

## Run

`main.py` (Python 3.13, stdlib only, no network) writes the single entry line to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

The program validates the gate itself (1–320 Unicode code points, single line, no control characters, no trailing newline) and verifies the write round-trips byte-for-byte.

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty — https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?ref=qjs4e9sj
