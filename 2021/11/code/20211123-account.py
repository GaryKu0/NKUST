# ask input username and password

LoginStatus = False
while LoginStatus == False:
    username = input("請輸入帳號：")
    password = input("請輸入密碼：")
    if username == "admin" and password == "123456":
        LoginStatus = True
        print("登入成功")
    else:
        print("登入失敗,請重試")
        LoginStatus = False

