from nonebot import on_command, CommandSession
import Technology.getTicketLinker as getTicketLinker
import user_db

# 防茉莉
loved_qq_numbers = [2782394649]

@on_command('ticket', aliases=('给我发卷','给我发券','给我发票'), only_to_me=False)
async def ticket(session: CommandSession ):
    # 参数预处理
    msg_content = session.current_arg_text.strip()
    ticketArgs = msg_content.split(' ')
    QQNumber = session.event['user_id']

    # 如果是茉莉发的，那剩下的全都不用整了直接回个6
    if (QQNumber in loved_qq_numbers):
        await session.send("6")
        return

    # 判断输入参数的长度
    provided_uid = None
    ticket_type = None

    if len(ticketArgs) == 2:  # 用户输入了 UID 和 ticketType
        provided_uid = ticketArgs[0]
        ticket_type = ticketArgs[1]
    elif len(ticketArgs) == 1:  # 用户只输入了 ticketType
        ticket_type = ticketArgs[0]
    else:
        await session.send("命令格式有误！")
        return

    # 查询已绑定的UID（如果有）
    maimaiUID = user_db.query_maimai_uid(QQNumber)

    # 如果用户输入了UID，优先使用输入的UID
    if provided_uid:
        if maimaiUID and provided_uid != maimaiUID:
            await session.send(
                f"将为 UID {provided_uid} 发票。"
            )
        maimaiUID = provided_uid
    else:
        # 如果没有输入UID且未绑定UID
        if not maimaiUID:
            await session.send("尚未绑定舞萌账号！请先绑定，或者直接附带 UID 参数")
            return
    # 验证
    if not ticket_type.isdigit() or len(ticket_type) != 1:
        await session.send("票类参数无效")
        return

    # 发送请求到 Linker 模块处理
    ticketGetResult = getTicketLinker.getTicket(maimaiUID,ticket_type)
    # 得出结果之后反馈结果
    reply_content = "结果: "+str(ticketGetResult)
    await session.send(reply_content)

