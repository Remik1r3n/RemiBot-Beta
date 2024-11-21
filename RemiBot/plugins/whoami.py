from nonebot import on_command, CommandSession

# 发票指令
@on_command('whoami', aliases=('看我','我是谁'), only_to_me=False)
async def ticket(session: CommandSession ):
    senderInfo = session.event['sender']
    print("DEBUG: User FULL info is: "+str(senderInfo))
    reply_content = '请问恁是 QQ 昵称为 ' + senderInfo['nickname'] + '，群名片为'+ senderInfo['card'] + '，QQ号为' + str(senderInfo['user_id']) + "的人🐎"
    await session.send(reply_content)

