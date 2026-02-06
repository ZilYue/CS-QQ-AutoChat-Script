# 截取屏幕图像
# 安装第三方库 Pillow

import pyautogui as pa


# pa.screenshot(imageFilename, region)
"""
截取屏幕图像
Args:
    imageFilename: 可以是文件路径什么的, 然后文件名: "C:\\Users\\yu_z_\\Pictures\\photo.png"
    region: 截图范围,左上角(x, y)到右下角(x, y). region好像默认全屏

Returns:

"""

# pa.alert(param, title, button)
"""
弹窗, 有暂停进程的作用. title和button的输入会警告,但是依然可以输入
Args:
    param: 主体内容
    title: 弹窗标题
    buttom: 弹窗的确定按钮

Returns:

"""


# def prompt(param, title, default):
"""
输入框, 也有暂停进程的作用
Args:
    param: 内容
    title: 标题
    default: 默认输入

Returns:
    输入的值
"""


