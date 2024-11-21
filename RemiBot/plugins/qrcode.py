from nonebot import on_command, CommandSession
import Technology.aimeDBLinker as aimeDBLinker
import json

@on_command('qrcode', aliases=('帮我扫码'), only_to_me=False)
async def qrcode(session: CommandSession ):
    msg_content = session.current_arg_text.strip()
    QQNumber = session.event['user_id']

    # 先简单检查格式是否正确
    if aimeDBLinker.qrcode_string_verify(msg_content):
        await session.send('尝试解析二维码……')
    else:
        await session.send('二维码格式错误')
        return
    
    # 然后发请求
    response_text = aimeDBLinker.maimaiQRCode_To_UID(msg_content)
    
    # 解析得到的数据
    try:
        response_data = json.loads(response_text)
        error_id = response_data.get("errorID")
        print("Error ID:", error_id)
    except json.JSONDecodeError as e:
        await session.send('无法解析返回的Json！网络问题？')

    # 结果
    match error_id:
        case 0:
            await session.send('成功扫码，得出 UID '+str(response_data.get("userID")))
        case 1:
            await session.send('无效的二维码')
        case 2:
            await session.send('二维码已过期') 
        case 50:
            await session.send('数据错误，可能是程序问题') 
        case _:
            await session.send('未知错误，请联系瑞米')

