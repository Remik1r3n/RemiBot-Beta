from nonebot import on_command, CommandSession


# 处理 bind 命令
@on_command('bind', aliases=('我要绑定'), only_to_me=False)
async def bind(session: CommandSession ):
    # 取得消息的内容，并且去掉首尾的空白符
    msg_content = session.current_arg_text.strip()
    print(session.current_arg)

    if not msg_content:
        await session.send('告诉我你的 UID，不然我绑定个鸡毛\n什么你不知道你的UID？问真正的瑞米去')
    else:
        if msg_content.isdigit():
            await session.send('什么 你的UID是'+msg_content+'？好的记下来了，但是绑不绑得看我心情')
        else:
            await session.send('我错了对不起')
