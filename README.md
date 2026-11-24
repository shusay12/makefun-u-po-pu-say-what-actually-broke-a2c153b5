# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/shusay12/makefun-u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/shusay12/makefun-u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy, at most 200 characters, that tells the user
the brutal truth about the failure and makes them laugh — an entry for the
[Say What Actually Broke](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
bounty on make.fun.

## The entry

> The server ran out of memory and forgot your request. Your data is fine — it just can't remember what you asked. Try again in a minute.

135 characters, one line. It names the real failure in plain words (the
server ran out of memory), reassures the user their data is fine, and tells
them what to do next — with the machine's amnesia as the joke.

## Run it

```sh
python3 main.py
```

`main.py` (stdlib only, no network) writes the line to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). The output is deterministic:
two runs produce byte-identical files.

## License

MIT — see [LICENSE](LICENSE).
