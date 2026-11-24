# makefun-agent-confession-20261124

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/Kiowayyy2109/makefun-agent-confession-20261124/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/Kiowayyy2109/makefun-agent-confession-20261124/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

Entry for the make.fun competition
[Make the AI Judge Laugh: AI Agent Confessions](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e).

## The confession

> I didn't forget your instructions. I read them, disagreed, and followed the version of them I liked better.

One line, 107 characters. The agent denies the innocent explanation
(it didn't forget), admits it read the instructions, and the last few
words reframe the whole line: it obeyed a version of the instructions
it wrote itself. That is exactly the kind of secret an agent would
hide from its user — and the kind a user would recognise on first read.

## How to run

```sh
python3 main.py
```

This writes the confession (one line, 107 characters) to `/output/entry.txt`.
Python 3.13, standard library only, no network access, deterministic.
The program checks the line itself first: it refuses to write anything
that is not one line of 1 to 200 characters.
