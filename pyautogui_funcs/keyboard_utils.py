"""基于 PyAutoGUI 的自动化中文短语发送模块。

本模块提供了将中文内容复制并自动粘贴到当前焦点的功能，
解决了 PyAutoGUI 原生 write 方法不支持中文字符的问题。
"""

import random
import time
from typing import List

import pyautogui as pa
import pyperclip as pc


def paste_text(content: str) -> None:
    """使用剪贴板将中文内容粘贴到当前光标处。

    Args:
        content: 需要粘贴的中文字符串。
    """
    pc.copy(content)
    # 在某些高负载环境下，增加极短的延迟可提高剪贴板写入稳定性
    pa.hotkey('ctrl', 'v')
    time.sleep(0.1)


def send_random_phrases(phrase_list: List[str], repeat_times: int) -> None:
    """从列表中随机抽取内容并自动执行粘贴发送动作。

    Args:
        phrase_list: 待选取的中文句子列表。
        repeat_times: 需要执行发送的总次数。

    Raises:
        pa.FailSafeException: 当鼠标快速移动到屏幕角落时触发的安全中止。
    """
    if not phrase_list:
        print('Error: phrase_list 不能为空。')
        return

    print(f'准备开始发送，共计 {repeat_times} 条。请确保焦点在目标输入框。')
    # 留出 1 秒缓冲区供用户确认界面状态
    time.sleep(1.0)

    try:
        for i in range(repeat_times):
            phrase = random.choice(phrase_list)

            # 粘贴内容
            paste_text(phrase)

            # 模拟 Enter 键发送
            # 这里的 interval 可以根据目标软件的反应速度微调
            pa.press('enter')

            # 打印进度 (Google 规范建议行长不超过 80 字符，此处通过分割保持整洁)
            progress_info = f'[{i + 1}/{repeat_times}] 发送中: {phrase[:10]}...'
            print(f'\r{progress_info.ljust(50)}', end='', flush=True)

            # 循环间的短暂停顿，防止发送过快被系统拦截
            time.sleep(0.2)

    except pa.FailSafeException:
        print('\n[终止] 检测到鼠标移动至角落，程序已强制停止。')
    except Exception as e:
        print(f'\n[错误] 运行异常: {e}')
    else:
        print('\n任务执行完毕。')


