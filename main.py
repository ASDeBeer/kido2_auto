import random
import time
import numpy as np
import os
from pyautogui import *
import pyautogui
import keyboard
import PIL
import cv2 as cv
from windowcapture import WindowCapture
import glob

blue = (0, 33, 584, 1076 - 33)
wincap = WindowCapture('BlueStacks App Player')

# entire screen
# im = pyautogui.screenshot(region=(0, 0, 1920, 1080))


# New Strat Check pixels


# Check shadow for tall or short    pyautogui.pixel()   pixel(198,995) (36, 27, 24)
# print(str(pyautogui.position()) + ': ' + str(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)))


def mouse_rgb():
    while True:
        if keyboard.is_pressed(' '):
            print(str(pyautogui.position()) + ': ' + str(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)))
            time.sleep(1)

# Get kid height
def kid_tall():
    start = time.time()
    while True:
        now = time.time()
        if now-start > 1:
            return False
        if pyautogui.pixel(198, 995) == (36, 27, 24):
            return True


# Check obstacle above head
def check_above_head(): # l=left r=right n=no
    if pyautogui.pixel(234, 743) == (167, 92, 42):
        return 'l'
    if pyautogui.pixel(351, 743) == (167, 92, 42):
        return 'r'
    return 'n'

def sign_rand(x):
    return random.randint(0,x*2)-x

def click_left():
    pyautogui.click(200+sign_rand(50), 500+sign_rand(50))

def click_right():
    pyautogui.click(200+sign_rand(50), 500+sign_rand(50))

print(sign_rand(50))
input('s')
#click left
#click right
#random sleep times
while True:
    print(pyautogui.pixel(234, 743))
    obs = check_above_head()
    if obs != 'n':
        print(obs)
input('s')
print(kid_tall())
# find img in img


input('kkkkkkk')

cv_screen = wincap.get_screenshot()
cv_screen = cv.cvtColor(cv_screen, cv.COLOR_BGR2GRAY)

kids = os.listdir('sprites/')

threshold = 0.3

while True:
    for kid in kids:
        kid = cv.imread('sprites/' + kid)
        try:
            r = cv.matchTemplate(cv_screen, kid, cv.TM_CCOEFF_NORMED)
        except:
            continue

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(r)

        if max_val >= threshold:
            print("ez")

# cv.imshow('image', tall)
# cv.waitKey(0)

input('Start screenshot collection?')

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

input('ll?')

# Karate Kido 2 Order of Operations

# General
# Click battle menu, Click battle
# jmp #Battle
# Click continue
# Click open reward/close
# jmp #General

# Battle
# Check tall or short kid
