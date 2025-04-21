import requests
import time
import sys

# ======= 用户配置 =======
student_id = ""  # 学号
operator = ""         # 运营商（cmcc=移动, njxy=电信, 空=校园网）
password = ""    # 密码

# ======= 构造账号信息 =======
def get_user_account(student_id, operator):
    return f",0,{student_id}@{operator}" if operator else f",0,{student_id}"

user_account = get_user_account(student_id, operator)

# ======= 发送登录请求 =======
url = "https://p.njupt.edu.cn:802/eportal/portal/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
params = {
    "callback": "dr1003",
    "login_method": "1",
    "user_account": user_account,
    "user_password": password
}

while True:
    try:
        req = requests.get(url, params=params, headers=headers)

        if req.text == 'dr1003({"result":0,"msg":"AC999","ret_code":2});':
            print("你已经登录到校园网哦~")
            break
        elif req.text == 'dr1003({"result":0,"msg":"运营商账号在线数超出限制，请联系运营商处理(Rad:Limit Users Err)","ret_code":1});':
            print("登录失败，你已经达到最大设备数，请至自助服务平台登出一个设备。")
        elif req.text == 'dr1003({"result":0,"msg":"账号或密码错误(ldap校验)","ret_code":1});':
            print("登录失败，用户名或密码错误，请检查您的信息。")
        elif req.text == 'dr1003({"result":0,"msg":"账号错误(运营商登录请检查输入的账号和绑定的运营商账号是否有误)","ret_code":1});':
            print("登录失败，您输入的运营商错误，请检查您的信息！")
        elif req.text == 'dr1003({"result":0,"msg":"本账号费用超支，禁止使用","ret_code":1});':
            print("登录失败，你没充网费啊awa")
        elif req.text == 'dr1003({"result":0,"msg":"运营商账号欠费或停机(Rad:Status_Err)","ret_code":1});':
            print("登录失败，电话是不是欠费了~")
        elif req.text == 'dr1003({"result":1,"msg":"Portal协议认证成功！"});':
            print("✅ 登录成功")
            break
        else:
            print("登录失败！未知错误！")
            print(f"返回信息: {req.text}")

    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {e}")
        sys.exit(1)  

    except Exception as e:
        print(f"发生异常: {e}")
        sys.exit(1)  

    time.sleep(3)
