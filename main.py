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

blue = (0, 33, 584, 1076 - 33)
wincap = WindowCapture('BlueStacks App Player')

#Globals
moves = []
s_s = 1.40625

def scr():
    sesh_id = input('Sesh ID: ')

    sc_folder = 'screenshots/'
    save_path = sc_folder + sesh_id + '/'

    sc_count = 0

    # q to quit
    while keyboard.is_pressed('q') == False:

        # Space for taking screenshots
        if keyboard.is_pressed(' '):
            screen = pyautogui.screenshot(region=blue)
            sc_name = str(sc_count) + '.png'
            screen.save(save_path + sc_name)
            sc_count = sc_count + 1


def mouse_rgb():
    while True:
        if keyboard.is_pressed(' '):
            print(str(pyautogui.position()) + ' with screen size - ' + str(s_s) + '  Color : ' + str(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)))
            time.sleep(1)

# Get kid height
def kid_tall():
    start = time.time()
    while True:
        now = time.time()
        if now-start > 1:
            return False
        if pyautogui.pixel(math.floor(198/s_s), math.floor(995/s_s)) == (36, 27, 24):
            return True


# Check obstacle above head
def check_above_head(): # l=left r=right n=no
    r = 'l'
    if pyautogui.pixel(math.floor(234/s_s), math.floor(743/s_s)) == (167, 92, 42):
        r = 'l'
        if pyautogui.pixel(math.floor(351/s_s), math.floor(743/s_s)) == (167, 92, 42):
            r = 'lr'
    elif pyautogui.pixel(math.floor(351/s_s), math.floor(743/s_s)) == (167, 92, 42):
        r = 'r'
    else:
        r = 'n'

    return r

def sign_rand(x):
    return random.randint(0,x*2)-x

def click_left():
    pyautogui.click(math.floor(200+sign_rand(10))/s_s, math.floor(743+sign_rand(3))/s_s)

def click_right():
    pyautogui.click(math.floor(400+sign_rand(10))/s_s, math.floor(743+sign_rand(3))/s_s)

def check_glass():
    return False

def check_mult():
    return False

def click_move(m):
    move = 'l'
    if m == 'n' and len(moves) > 1:
        if moves[len(moves)-1] != 'n':
            move = moves[len(moves)-1]
    elif m == 'l':
        move = 'l'
    elif m == 'r':
        move = 'r'

    if move == 'l':
        click_left()
    elif move == 'r':
        click_right()

def click_continue():
    pyautogui.click(math.floor(300+sign_rand(10))/s_s, math.floor(743+sign_rand(3))/s_s)

def click_open_reward():
    pyautogui.click(math.floor(300+sign_rand(10))/s_s, math.floor(1050+sign_rand(3))/s_s)

def click_close():
    pyautogui.click(math.floor(300+sign_rand(10))/s_s, math.floor(1050+sign_rand(3))/s_s)

def click_play():
    pyautogui.click(math.floor(300+sign_rand(10))/s_s, math.floor(850+sign_rand(3))/s_s)

def game_ongoing():
    if pyautogui.pixel(math.floor(300/s_s), math.floor(260/s_s)) == (255, 255, 255):
        print('Game Started')
        return False
    return True

def game_started():
    while True:
        if pyautogui.pixel(math.floor(75/s_s), math.floor(840/s_s)) == (255, 255, 255):
            print('Game Started')
            return True


def play():
    h = 2
    prev = 'n'
    m = 'n'
    if kid_tall():
        h = 2
    else:
        h = 1

    time.sleep((random.randint(0,10)+10)/10) #1-2 s
    while(game_ongoing()):
        time.sleep((random.randint(0,1)+2)/10) #0.2-0.3 s
        prev = m
        m = check_above_head()
        click_move(m)
        moves.append(m)
        time.sleep((random.randint(0,1)+3)/10) #0.3

    time.sleep((random.randint(0,10)+10)/10) #1-2 s
    click_continue()


def loop(args):
    if(args==0):
        while True:
            return 0

    else:
        time.sleep((random.randint(0,10)+10)/10) #1-2 s
        click_play()
        time.sleep(5)
        game_started()
        time.sleep((random.randint(0,10)+10)/10) #1-2 s
        play()
        time.sleep((random.randint(0,10)+10)/10) #1-2 s
        click_open_reward()
        time.sleep((random.randint(0,10)+10)/10) #1-2 s
        click_close()   
        time.sleep((random.randint(0,10)+10)/10) #1-2 s



loop(input("Loop count? 0=inf | ~"))
