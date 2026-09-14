#!/usr/bin/env python3
"""Geek-style terminal Snake. Run: python3 snake.py"""
import curses
import random

SNAKE_CH = "#"
HEAD_CH = "@"
FOOD_CH = "0"

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_WHITE, -1)

    sh, sw = stdscr.getmaxyx()
    h, w = sh - 2, sw - 1  # leave room for border + status line

    snake = [(h // 2, w // 4 + i) for i in range(3)][::-1]
    direction = (0, 1)
    food = spawn_food(snake, h, w)
    score = 0
    delay = 120  # ms, decreases with score
    stdscr.timeout(delay)

    while True:
        key = stdscr.getch()
        new_dir = {
            curses.KEY_UP: (-1, 0), curses.KEY_DOWN: (1, 0),
            curses.KEY_LEFT: (0, -1), curses.KEY_RIGHT: (0, 1),
            ord('w'): (-1, 0), ord('s'): (1, 0),
            ord('a'): (0, -1), ord('d'): (0, 1),
        }.get(key)
        if key in (ord('q'), 27):
            break
        if new_dir and (new_dir[0] * -1, new_dir[1] * -1) != direction:
            direction = new_dir

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (head[0] <= 0 or head[0] >= h or head[1] <= 0 or head[1] >= w
                or head in snake):
            game_over(stdscr, score)
            return

        snake.insert(0, head)
        if head == food:
            score += 10
            food = spawn_food(snake, h, w)
            delay = max(40, delay - 4)
            stdscr.timeout(delay)
        else:
            snake.pop()

        draw(stdscr, snake, food, score, h, w)


def spawn_food(snake, h, w):
    while True:
        pos = (random.randint(1, h - 1), random.randint(1, w - 1))
        if pos not in snake:
            return pos


def draw(stdscr, snake, food, score, h, w):
    stdscr.erase()
    border = curses.color_pair(3)
    stdscr.attron(border)
    stdscr.border()
    stdscr.attroff(border)

    stdscr.addstr(0, 2, f"[ SNAKE.exe | score: {score:04d} | len: {len(snake):03d} ]", border)

    stdscr.attron(curses.color_pair(2))
    stdscr.addch(food[0], food[1], FOOD_CH)
    stdscr.attroff(curses.color_pair(2))

    stdscr.attron(curses.color_pair(1))
    for i, (y, x) in enumerate(snake):
        ch = HEAD_CH if i == 0 else SNAKE_CH
        try:
            stdscr.addch(y, x, ch)
        except curses.error:
            pass
    stdscr.attroff(curses.color_pair(1))

    stdscr.addstr(h + 1, 2, "wasd/arrows move | q quit", curses.color_pair(3))
    stdscr.refresh()


def game_over(stdscr, score):
    stdscr.nodelay(False)
    stdscr.erase()
    sh, sw = stdscr.getmaxyx()
    msg = f"GAME OVER — final score: {score}"
    prompt = "press any key to exit"
    stdscr.attron(curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(sh // 2 - 1, max(0, (sw - len(msg)) // 2), msg)
    stdscr.attroff(curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(sh // 2 + 1, max(0, (sw - len(prompt)) // 2), prompt, curses.color_pair(3))
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
