#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands -- entry program.

Writes exactly one joke about cats, one line, to ``entry.txt`` inside
``$OUTPUT_DIR`` (default ``/output``).  The program is fully deterministic:
it always writes the same text, with no randomness, no network and no
clock input, so two runs produce byte-identical output.

Gate: the file must be UTF-8 text of 1-200 characters and not only
whitespace, so the program raises hard if the chosen joke ever falls
outside that range.  No trailing newline is written: the file content
is exactly the joke, one line, nothing else.

Three candidate jokes, judged against the brief (setup + turn that
lands; laugh out loud on first read; surprise / misdirection / fresh
angle, not a stale pun; short, no padding; retellable the same day):

Varian A -- "My cat stares at the wall for an hour every night, and
honestly, at this point I'm starting to believe him."
  Setup: kucing menatap tembok (trope "kucing melihat hantu").
  Twist: pemiliknya mulai percaya.  Lucu dan segar, tapi twist-nya
  lebih ke arah "pintar" daripada tertawa terbahak; gambarnya abstrak
  (percaya pada apa, tidak kelihatan) sehingga kurang nempel di
  bacaan pertama.

Varian B -- "I caught my cat watching me sleep -- he didn't blink, he
just pressed my face like a snooze button."
  Setup: kucing mengawasi pemilik tidur (seram, bikin penasaran).
  Twist: dia menekan wajah pemilik seperti tombol snooze.  Gambarnya
  langsung kebayang (fisik, visual), twist mendarat di dua kata
  terakhir, dan sudutnya segar: kucing memperlakukan manusia seperti
  alarm.  Paling gampang diceritakan ulang ke teman.  Versi akhir
  dipangkas "last night"-nya supaya lebih ringkas tanpa kehilangan
  apa pun.  -> TERPILIH.

Varian C -- "The vet said my cat is overweight; my cat said the vet is
lucky he can't reach the keyboard to leave a review."
  Setup: dokter hewan bilang kucing kegemukan.  Twist: kucing akan
  memberi ulasan buruk kalau bisa menjangkau keyboard.  Sudut segar
  (kucing sebagai pelanggan marah), tapi setup-nya paling panjang dan
  punchline-nya lebih "cerdas" daripada mengundang tawa; ritmenya
  kalah ringkas dari B.

Keputusan: varian B.  Paling nempel tema (kucing + manusia), paling
orisinal (hindari klise: menjatuhkan barang, mengabaikan pemilik,
laser pointer, kotak kardus -- tidak satu pun dipakai), paling
berkesan di bacaan pertama, dan twist mendarat di kata terakhir
("snooze button").
"""

import os
import sys

# The chosen joke (variant B).  One line, ASCII + one em dash.
# Tightened: "last night" cut -- it added nothing the setup does not
# already imply, and the joke lands faster without it.
JOKE = (
    "I caught my cat watching me sleep \u2014 "
    "he didn't blink, he just pressed my face like a snooze button."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    # Gate check first: fail hard rather than ever writing a bad entry.
    length = len(JOKE)
    if not (MIN_CHARS <= length <= MAX_CHARS):
        raise ValueError(
            "joke is %d characters, outside the 1-200 gate" % length
        )
    if not JOKE.strip():
        raise ValueError("joke is only whitespace")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Exactly the joke, no trailing newline: the file is one line and
    # nothing else, so its character count is the joke's count.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
