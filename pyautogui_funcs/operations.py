import pyautogui as pg
import pyperclip as pc
import time
from pynput.keyboard import Key, Controller, Listener
import cv2

from pyautogui_funcs import keyboard_utils as key
from pyautogui_funcs import mouse_utils as mouse
from pyautogui_funcs import phrases


keyboard = Controller()


def open_apps(software: str):
    pg.hotkey('alt', 'space')
    time.sleep(1)
    pc.copy(str(software))
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    time.sleep(5)


def left_screen():
    pg.hotkey('win', 'left')
    time.sleep(0.5)


def qq_search(name: str):
    qq_search_icon = r"pyautogui_funcs/qq-photos/qq_search.png"
    qq_search_icon_center = find_pos(qq_search_icon)

    if qq_search_icon_center:
        pg.click(qq_search_icon_center)
        key.paste_text(name)
        time.sleep(1.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        print("搜索失败")

    time.sleep(1.5)


def find_pos(filename):
    try:
        # 尝试寻找图片
        pos = pg.locateOnScreen(filename, confidence=0.8)  # 建议加上相似度
        return pg.center(pos)
    except pg.ImageNotFoundException:
        # 如果没找到，不让程序崩溃，而是返回 None
        print(f"在屏幕上没找到图标: {filename}")
        return None


def open_signed_qq():
    qq_icon_small = r"pyautogui_funcs/qq-photos/qq_signed.png"
    qq_icon_large = r"pyautogui_funcs/qq-photos/qq_icon.png"
    qq_icon_small_center = find_pos(qq_icon_small)
    qq_icon_large_center = find_pos(qq_icon_large)

    if qq_icon_small_center:
        pg.click(qq_icon_small_center)
    elif qq_icon_large_center:
        pg.click(qq_icon_large_center)
    else:
        print("没有找到qq图标, 打开失效")

    time.sleep(1)


def qq_chat_box(phrases: list, repeat_times: int):
    chat_box = find_pos(r"pyautogui_funcs/qq-photos/qq_chat_box.png")

    if chat_box:
        pg.click(chat_box)
        key.send_random_phrases(phrases, repeat_times)
        time.sleep(0.1)
    else:
        print("没找到聊天框")


def send_long(repeat_times: int):
    key.send_random_phrases(phrases.long, repeat_times)


def send_ez(repeat_times: int):
    key.send_random_phrases(phrases.ez, repeat_times)


def send_dirty(repeat_times: int):
    key.send_random_phrases(phrases.dirty, repeat_times)


def send_nb(repeat_times: int):
    key.send_random_phrases(phrases.nb, repeat_times)


def send_ez(repeat_times: int):
    key.send_random_phrases(phrases.ez, repeat_times)


def cs_chat_box(phrases: list, repeat_times: int):
    chat_box_img = r"pyautogui_funcs/CS2-scrshot/in-game/chat_box.png"

    for i in range(repeat_times):
        # 1. 每次循环都尝试找一次聊天框
        chat_box_center = find_pos(chat_box_img)

        # 2. 如果没找到，说明聊天框没开启，按 'y' 呼出
        if not chat_box_center:
            pg.press("y")
            # time.sleep(0.05)  # 给一点动画缓冲时间
        else:
            # 如果找到了，点一下确保激活焦点
            pg.click(chat_box_center)
            # time.sleep(0.05)

        # 3. 发送短语
        # 注意：确保 send_random_phrases 内部执行了按下 'Enter' 的动作
        key.send_random_phrases(phrases, 1)

        # 4. 关键：CS2 输入后聊天框会自动消失，给系统一点反应时间
        # time.sleep(0.5)


def cs_chat_box_long(repeat_times: int):
    cs_chat_box(phrases.long, repeat_times)


def cs_chat_box_ez(repeat_times: int):
    cs_chat_box(phrases.ez, repeat_times)


def cs_chat_box_nb(repeat_times: int):
    cs_chat_box(phrases.nb, repeat_times)


def open_signed_cs():
    pg.press("win")
    cs_icon = find_pos(r"pyautogui_funcs/CS2-scrshot/cs_icon.png")

    if cs_icon:
        pg.click(cs_icon)
        time.sleep(0.5)
    else:
        print("cs没有打开")

