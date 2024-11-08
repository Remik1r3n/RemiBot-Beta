# RemiBot 主程序
# 由 Remik1⭐ 于 2024 年末携爱敬上
# 版权所无 Copyleft 2024 Remik1. No rights reserved.

from os import path
import nonebot
import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()

    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'RemiBot', 'plugins'), 'RemiBot.plugins'
    )

    nonebot.run()
