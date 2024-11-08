from nonebot import on_command, CommandSession
import getTicketLinker

# 发票指令
@on_command('ticket', aliases=('给我发卷','给我发券','给我发票'), only_to_me=False)
async def ticket(session: CommandSession ):
    await session.send("开始尝试发票。如果没了下文，那就是发票失败，请联系瑞米")
    # 处理参数
    msg_content = session.current_arg_text.strip()
    ticketArgs = msg_content.split(' ')
    # 发送请求到 Linker 模块处理
    ticketGetResult = getTicketLinker.getTicket(ticketArgs[0],ticketArgs[1])
    # 得出结果之后反馈结果
    reply_content = "结果: "+str(ticketGetResult)
    await session.send(reply_content)

