from nonebot import on_command, CommandSession

# 回骂
@on_command('dissme', aliases=('操你妈', '傻逼', '傻逼吧', '你妈死了', 'sb', '我草你妈'), only_to_me=True)
async def diss(session: CommandSession ):
    reply_content = "哦6"

    await session.send(reply_content)

