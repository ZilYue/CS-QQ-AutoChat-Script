import time

import pyautogui as pa
from pynput import mouse


def edge():
    print("\n---------------------------------------\n")


def print_cur_coordinates():
    x, y = pa.position()
    print(f"mouse at ({x}, {y})")


def print_cur_screen_size():
    w, h = pa.size()
    print(f"current screen size: ({w}, {h})")


def is_safe(*, x, y):
    """
    判断鼠标指针是否在屏幕内.

    Args:
        x: 鼠标指针横坐标.
        y: 鼠标指针纵坐标.

    Returns:
        如果安全则返回True.
    """
    width, height = pa.size()
    return 0 <= x < width and 0 <= y < height


def realtime_mouse_position():
    """实时监控鼠标指针位置并在控制台更新。"""
    try:
        # 初始化位置
        pre_x, pre_y = pa.position()
        print("开始监控... ")

        while True:
            x, y = pa.position()

            # 使用 or：只要横向或纵向动了，就更新
            if x != pre_x or y != pre_y:
                pre_x, pre_y = x, y
                # \r 回到行首，end="" 不换行，实现原地刷新
                print(f"\rCurrent Position: ({x}, {y})".ljust(30), end="")

            # 释放 CPU 压力，0.05s - 0.1s 体验最佳
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n监控已停止。")


def move_mouse_to(*, x: int, y: int, duration: float = 0):
    """鼠标指针绝对移动。

    将鼠标指针从当前位置移动到屏幕上的绝对坐标 (x, y)。

    Args:
        x: 指针移动目标横坐标（像素）。
        y: 指针移动目标纵坐标（像素）。
        duration: 移动过程持续的时间（秒）。
    """
    print("Executing: move_mouse_to_input...")

    if is_safe(x=x, y=y):
        pa.moveTo(x, y, duration=duration)
        print_cur_coordinates()
    else:
        print("Error: Target coordinates out of screen bounds.")
        print_cur_screen_size()


def move_mouse(*, dx: int, dy: int, duration: float = 0):
    """鼠标指针相对移动。

    基于当前鼠标指针位置，增加偏移量 dx 和 dy 进行移动。

    Args:
        dx: 横坐标相对移动偏移量（像素）。
        dy: 纵坐标相对移动偏移量（像素）。
        duration: 移动过程持续的时间（秒）。
    """
    print("Executing: move_mouse_from_input...")

    curr_x, curr_y = pa.position()
    target_x = curr_x + dx
    target_y = curr_y + dy

    if is_safe(x=target_x, y=target_y):
        pa.moveTo(target_x, target_y, duration=duration)
        print_cur_coordinates()
    else:
        print("Error: Relative move would exceed screen boundaries.")


# pa.click(x, y, clicks, interval, button, duration)
    """
    鼠标点击,但是建议先用moveTO再点击
    Args:
        x: 鼠标指针目标横坐标
        y: 鼠标指针目标纵坐标
        clicks: 鼠标点击次数
        interval: 鼠标点击间隔时间 
        button: 鼠标点击的按键, 可选: "left", "right", "middle"
        duration: 鼠标指针移动时间
    """


# pa.mouseDown(), pa.mouseUp()
    """
    按住鼠标按键和抬起鼠标按键
    可以配合time.sleep使用
    Args:
        x: 鼠标指针目标横坐标
        y: 鼠标指针目标纵坐标
        button: 鼠标点击的按键, 可选: "left", "right", "middle"
    """


# pa.scroll(clicks)
    """
    鼠标滚轮滑动
    Args:
        clicks: 滑动距离和方向, 正数向上, 负数向下
    """