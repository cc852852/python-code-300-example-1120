import time
def show_info():
    print('输入提示的数字，执行相应的操作：0.退出 1.查看登录日志')

#记录日志
def write_logininfo(username):
    with open('log.txt','a') as file:
        s=f'用户名：{username},登录时间：{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
