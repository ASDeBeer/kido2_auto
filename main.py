import random
import time
import numpy as np
import os
from pyautogui import *
import pyautogui
import keyboard
import cv2 as cv
from windowcapture import WindowCapture
import glob
import math
import json

# Globals

s_s = 1
prev_move = 'l'

global l_loc
global r_loc

global moves

opt = False
l_loc = []
r_loc = []
merge = []

moves = []

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

targets = []
for x in range(0, len(str(data))):
    if x % 3 == 0:
        targets.append(int(str(data)[x] + str(data)[x + 1] + str(data)[x + 2]))


def scr():
    sesh_id = input('Sesh ID: ')

    sc_folder = 'screenshots/'
    save_path = sc_folder + sesh_id + '/'

    sc_count = 0

    # q to quit
    while keyboard.is_pressed('q') == False:
        blue = (0, 33, 584, 1076 - 33)
        # Space for taking screenshots
        if keyboard.is_pressed(' '):
            screen = pyautogui.screenshot(region=blue)
            sc_name = str(sc_count) + '.png'
            screen.save(save_path + sc_name)
            sc_count = sc_count + 1


def mouse_rgb():
    while True:
        if keyboard.is_pressed(' '):
            print(str(pyautogui.position()) + ' with screen size - ' + str(s_s) + '  Color : ' + str(
                pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)))
            time.sleep(1)


# Get kid height
def kid_tall():
    start = time.time()
    while True:
        now = time.time()
        if now - start > 1:
            return False
        if pyautogui.pixel(math.floor(198 / s_s), math.floor(995 / s_s)) == (36, 27, 24):
            return True


def to_json(yy):
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(data)
    print(yy)
    if str(yy) not in str(data):
        with open('data.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(yy, ensure_ascii=False))


# sensei (x=234, y=743)
# short (x=246, y=801)
# rambo (x=236, y=762)
# gi  (x=236, y=772)


# OBSTACLE RGB (167, 92, 42)
# MULT OBSTACLE RGB (129, 113, 130)
# Check obstacle above head
def check_above_head():  # l=left r=right n=no return best move
    r = 'n'
    global r_loc
    global l_loc

    # Check known yy

    for loc in targets:
        if pyautogui.pixel(234, loc) == (167, 92, 42):
            r = 'l'
            return r
        if pyautogui.pixel(234, loc) == (129, 113, 130):
            r = 'll'
            return r
        if pyautogui.pixel(351, loc) == (167, 92, 42):
            r = 'r'
            return r
        if pyautogui.pixel(351, loc) == (129, 113, 130):
            r = 'rr'
            return r
    return r
    print('not found')
    r1 = 750
    r2 = 770
    for yy in range(int(r1 / 1), int(r2 / 1)):
        yy = int(yy * 1)
        if pyautogui.pixel(math.floor(234 / s_s), math.floor(yy / s_s)) == (167, 92, 42):
            r = 'l'
            to_json(yy)
            return r
        elif pyautogui.pixel(math.floor(351 / s_s), math.floor(yy / s_s)) == (167, 92, 42):
            r = 'r'
            to_json(yy)
            return r
        if len(moves) > 50:
            if pyautogui.pixel(math.floor(234 / s_s), math.floor(yy / s_s)) == (129, 113, 130):
                r = 'll'
                to_json(yy)
                return r
            elif pyautogui.pixel(math.floor(351 / s_s), math.floor(yy / s_s)) == (129, 113, 130):
                r = 'rr'
                to_json(yy)
                return r

    return r


def sign_rand(x):
    return random.randint(0, x * 2) - x


def click_left():
    pyautogui.click(math.floor(200 + sign_rand(10)) / s_s, math.floor(743 + sign_rand(3)) / s_s)


def click_right():
    pyautogui.click(math.floor(400 + sign_rand(10)) / s_s, math.floor(743 + sign_rand(3)) / s_s)


def check_glass():
    return False


def check_mult():
    return False


def click_move(m):
    mov = m
    if mov == 'rr':
        click_left()
        time.sleep((random.randint(0, 1) + 60) / 1000)
        click_left()
        time.sleep((random.randint(0, 1) + 60) / 1000)
        click_left()
    if mov == 'll':
        click_right()
        time.sleep((random.randint(0, 1) + 60) / 1000)
        click_right()
        time.sleep((random.randint(0, 1) + 60) / 1000)
        click_right()

    if mov == 'r':
        click_left()
    if mov == 'l':
        click_right()
    if mov == 'n':
        if moves[len(moves) - 1] == 'r':
            click_left()
        elif moves[len(moves) - 1] == 'l':
            click_right()
        else:
            click_left()


def click_continue():
    pyautogui.click(math.floor(300 + sign_rand(10)) / s_s, math.floor(743 + sign_rand(3)) / s_s)


def click_open_reward():
    pyautogui.click(math.floor(300 + sign_rand(10)) / s_s, math.floor(1050 + sign_rand(3)) / s_s)


def click_close():
    pyautogui.click(math.floor(300 + sign_rand(10)) / s_s, math.floor(1050 + sign_rand(3)) / s_s)


def click_play():
    pyautogui.click(math.floor(330 + sign_rand(10)) / s_s, math.floor(940 + sign_rand(3)) / s_s)


def click_rate():
    pyautogui.click(math.floor(300 + sign_rand(10)) / s_s, math.floor(743 + sign_rand(3)) / s_s)


def game_ongoing():
    if pyautogui.pixel(math.floor(502 / s_s), math.floor(104 / s_s)) == (37, 22, 68):
        print("Game Ended")
        return False
    return True


def game_started():
    while True:
        if pyautogui.pixel(math.floor(90 / s_s), math.floor(900 / s_s)) == (255, 255, 255):
            print('Game Started')
            return True


def play():
    global r_loc
    global l_loc
    global moves
    moves = ['l']

    h = 2
    m = 'l'
    moves.append('l')
    time.sleep((random.randint(0, 1) + 5) / 10)  # 1-2 s
    while game_ongoing():
        m = check_above_head()
        click_move(m)
        moves.append(m)
        time.sleep((random.randint(0, 1) + 30) / 1000)

    time.sleep((random.randint(0, 10) + 10) / 10)  # 1-2 s
    click_continue()


def loop(args):
    if args == 'inf':
        while True:
            click_close()
            time.sleep((random.randint(0, 1) + 5) / 10)  # 1-2 s
            click_play()
            time.sleep(5)
            game_started()
            time.sleep((random.randint(0, 1) + 5) / 10)  # 1-2 s
            play()
            time.sleep((random.randint(0, 1) + 5) / 10)  # 1-2 s
            click_open_reward()
            time.sleep((random.randint(0, 1) + 5) / 10)  # 1-2 s
            click_rate()


    else:
        time.sleep((random.randint(0, 10) + 10) / 10)  # 1-2 s
        click_play()
        time.sleep(5)
        game_started()
        time.sleep((random.randint(0, 10) + 10) / 10)  # 1-2 s
        play()
        time.sleep((random.randint(0, 10) + 10) / 10)  # 1-2 s
        click_open_reward()
        time.sleep((random.randint(0, 10) + 10) / 10)  # 1-2 s
        click_close()
        time.sleep((random.randint(0, 10) + 10) / 10)  # 1-2 s
        click_rate()
        time.sleep((random.randint(0, 10) + 10) / 10)  # 1-2 s
        click_close()


# n = input("Loop count? (inf/num) | ~")
loop('inf')

exit(0)
