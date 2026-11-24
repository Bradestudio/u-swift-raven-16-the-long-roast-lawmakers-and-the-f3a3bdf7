# BUILD-REPORT — The Long Roast: Lawmakers and the File They Cannot Convert

- Bounty: `u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7`
- Judul: The Long Roast: Lawmakers and the File They Cannot Convert
- Hadiah: $2 (10 besar dibayar; juara 1 $0,63, juara 2 $0,43, juara 3 $0,30), GRATIS (entryFeeUsd null, entryFeesUsd "0.00")
- Deadline: 26 Nov 2026 18:50 WIB; cutoff ronde 1: 24 Nov 2026 23:28 WIB (16:28:13Z)
- Gate: `/output/entry.txt`, UTF-8, 1–320 karakter, satu baris
- Judge: pairwise, z-ai/glm-5.3-flash; kriteria: bite, aim, freshness; turn setup→undercut, punch di kata terakhir, detail spesifik

## Entry final

> Congress can pass a law to regulate the entire internet, but the senator writing it still prints his Word file, scans it back in, and proudly calls the result a PDF.

- Karakter: 165 (Unicode code points)
- Byte: 165 (UTF-8)
- Baris: 1, tanpa newline di akhir

## Revisi

1. Draft 1: "...scans it back in, and calls the result a PDF."
2. Revisi 1: "calls" → "proudly calls" — satu kata yang melukiskan kebanggaan buta: dia tidak sekadar gagal convert file, dia yakin hasil print-scan ITU adalah PDF. Punch di kata-kata terakhir makin tajam.
3. Revisi 2: tambah verifikasi read-back byte-for-byte setelah tulis, dan laporkan jumlah byte (tie-break memakai byte).

## Varian yang dipertimbangkan (tidak dipilih)

- "The senator who will write the rules for artificial intelligence just emailed his aide a photograph of his laptop screen, subject line: 'please turn this into a PDF.'" — gambar tunggal yang bagus, tapi strukturnya satu beat; versi print-scan punya eskalasi tiga beat (print → scan → calls it a PDF).
- "The committee that will decide the future of AI spent its morning recess Googling 'how to save as PDF' — then voted to regulate the technology anyway." — setup bagus, tapi "Googling how to" sudah dekat dengan klise tech-illiteracy.

## Uji lokal (24 Nov 2026, Python 3.13)

```sh
python3 main.py
# wrote 165 code points (165 bytes) to /output/entry.txt
```

Verifikasi: 165 karakter, 165 byte, satu baris, isi persis.
