import itchat
import get_ans
from itchat.content import TEXT
import time

@itchat.msg_register([TEXT])
def get_message(msg):
    # 获取发送者的名称与消息
    username = msg['FromUserName']
    message = msg['Text']

    # 获取发送信息者的昵称
    userinfo = itchat.search_friends(userName=username)
    nickname = userinfo['NickName']

    print(f"收到来自{nickname}的消息：{message}")

    #p.send(nickname,False,message)

    # 获取回答
    ans=get_ans.answer_message(username,message)

    print(f"回复{nickname}：{ans}")

    #p.send(nickname,True,ans)

    itchat.send(ans, toUserName=username)

# 登录微信

itchat.auto_login()
print("开始启动微信")
itchat.run()
time.sleep(1)