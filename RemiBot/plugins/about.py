from nonebot import on_command, CommandSession
import platform

# 关于
@on_command('about', aliases=('你是谁'), only_to_me=False)
async def about(session: CommandSession ):
    profile = ['architecture','machine','node','platform','python_build','python_compiler','python_version','release','system','version',]

    reply_content = "This is RemiBot, Made with ♥ by Remik1.\nCurrent environment：\n"

    for key in profile:
        if hasattr(platform, key):
            reply_content = reply_content + key + ": " + str(getattr(platform, key)()) + "\n"

    await session.send(reply_content)
            
