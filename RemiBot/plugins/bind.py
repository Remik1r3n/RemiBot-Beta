from nonebot import on_command, CommandSession
import user_db

@on_command('bind', aliases=('我要绑定'), only_to_me=False)
async def bind(session: CommandSession ):
    msg_content = session.current_arg_text.strip()
    QQNumber = session.event['user_id']
    
    if not msg_content:
        await session.send('可使用 “瑞米帮我扫码 (二维码内容)” 命令，从二维码解析出 UID')
    else:
        if msg_content.isdigit():
            user_db.bind_or_update_user(str(QQNumber),str(msg_content))
            await session.send('已将 QQ 号 '+str(QQNumber)+" 和 UID "+str(msg_content)+" 进行绑定。")
        else:
            await session.send('UID 格式似乎无效。')
