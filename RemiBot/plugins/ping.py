from nonebot import on_command, CommandSession


# 回应Ping
@on_command('ping', aliases=('呢'), only_to_me=False)
async def ping(session: CommandSession ):
    # 取得消息的内容，并且去掉首尾的空白符
    msg_content = session.current_arg_text.strip()

    if not msg_content:
        await session.send('我在')
    else:
        reply_content = msg_content
        reply_content = reply_content.replace("我", "TEMP_ME")
        reply_content = reply_content.replace("你", "我")
        reply_content = reply_content.replace("TEMP_ME", "你")
        reply_content = reply_content.replace("吗", "")
        await session.send("我在，不"+reply_content+"！")
    
