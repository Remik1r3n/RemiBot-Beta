from nonebot import on_command, CommandSession
import user_db

@on_command('checkbind', aliases=('查询绑定'), only_to_me=False)
async def checkbind(session: CommandSession ):
    QQNumber = session.event['user_id']
    result = user_db.query_maimai_uid(QQNumber)

    if result:
        await session.send(f'查询结果：{result}')
    else:
        await session.send('查询失败')