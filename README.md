# CS-QQ-AutoChat-Script
一个基于 Python 的自动化工具，支持在 CS2 游戏内和 QQ 窗口自动发送预设的中文字符串，支持自定义频率和短语库。

## 🌟 功能特点
- **智能检测**：自动识别 CS2 聊天框状态，若未唤起则自动按 `Y` 呼出。
- **中文支持**：解决游戏内无法直接输入中文的问题。
- **高度自定义**：支持自定义话术库和循环次数。
- **多平台适配**：除 CS2 外，也可用于 QQ 等聊天工具的自动刷屏/消息发送。

## 📂 项目结构
```text
.
├── CS2-scrshot/       # 存放用于图像识别的 chat_box 截图
├── qq-photos/         # 存放 QQ 窗口相关的识别截图
├── operations.py      # 核心逻辑：包含 cs_chat_box 等主循环函数
├── phrases.py         # 话术配置：在这里修改你的中文句子列表
├── keyboard_utils.py  # 键盘输入封装
├── screen_utils.py    # 屏幕识别与坐标检测封装
└── mouse_utils.py     # 鼠标操作封装
