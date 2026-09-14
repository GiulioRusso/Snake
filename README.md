# Snake

Geek-style terminal Snake game, built with Python's `curses`. No dependencies.

```
[ SNAKE.exe | score: 0040 | len: 007 ]
┌──────────────────────────────┐
│                               │
│      ###@                    │
│                       0       │
│                               │
└──────────────────────────────┘
 wasd/arrows move | q quit
```

## Requirements

- Python 3
- A terminal with `curses` support (built into Python on macOS/Linux; on
  Windows install `windows-curses` via `pip install windows-curses`)

## Run

```bash
python3 snake.py
```

## Controls

| Key            | Action    |
|----------------|-----------|
| `W`/`A`/`S`/`D` or arrow keys | Move |
| `Q` or `Esc`   | Quit      |

Speed increases as your score grows. Hitting a wall or yourself ends the game.

## License

MIT — see [LICENSE](LICENSE).
