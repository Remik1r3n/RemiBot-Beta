import os

def getTicket(uid, ticketType):
    # 运行当前目录的 getTicket.jar 来发票
    command = f'java -jar "{os.path.join(os.getcwd(), "getTicket.jar")}" "{uid}" "1" "{ticketType}"'
    print("About to run command: "+command)
    result = os.system(command)

    # 报错的文案
    ErrorNumbers = {
        0: "好耶！成功发票！",
        1: "系统错误，没有成功调用程序。请联系瑞米。",
        2: "你似乎没下号，但可能发票成功了。",
        10: "登陆失败，请在公众号内点击获取新的二维码，然后再试。",
        11: "获取失败，账号似乎在小黑屋内？",
        12: "登陆成功，但获取失败。可能是账号内已有此票？",
        13: "下号失败，而且账号可能被关进小黑屋了 :(",
        20: "程序报告了很奇怪的异常。请联系瑞米。",
        21: "程序报告了参数无效。请联系瑞米。",
        22: "程序报告了参数不够。请联系瑞米。",
    }

    return ErrorNumbers[result]
