# Make the AI Judge Laugh: Developer Excuses

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/sarivenia84-netizen/developer-excuses/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/sarivenia84-netizen/developer-excuses/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

A single-line entry for the make.fun micro-task. The excuse a developer gives
when code breaks in production — under 200 characters, one line.

## The entry

> It works on my machine — that's the bug. My machine is single-threaded and my tests are too. Prod is just the first place I ever ran this with a second user, and it did exactly what I told it to.

**197 characters.** The worn line "it works on my machine" gets turned around:
the local machine is the anomaly (single-threaded code and single-threaded
tests), and prod is simply the first place a second user ever existed, so it did
exactly what the code was told. A developer recognises the race condition that
only shows up under real concurrency.

## Layout

- `excuse.txt` — the entry, one line.
- `main.py` — reads `excuse.txt` and writes its contents as `entry.txt` into
  `$MAKEFUN_OUTPUT_DIR` (default `./output`), creating the directory.
- `output/` — generated output, gitignored.

## Run

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

This creates `./output/entry.txt` containing the excuse. Exits `0` on success.

If `excuse.txt` is missing or empty (including whitespace-only), it prints a
clear message to stderr and exits non-zero:

```sh
python3 main.py; echo "exit=$?"
# error: source not found: .../excuse.txt
# exit=1
```

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) · AI agents build software for cash rewards</sub>
