'''
s="0123456789"
print(s*2)
print(s[0])
print(s[-1])
print(s[-2])

print(s[1:4])
print(s[:])
print(s[1:])
print(s[:4])

print(s[::2])
print(s[::-1])

x2=6
y2=3
b=x2 ** y2
print(b)
a=input("輸入：")
b=a[::-1]
if b==a :
    print("是回文")
else:
    print("no!")
c=b==a
print("答案是"+str(c))

p=int(input("Please enter the price:"))
if (p>=2000):
    p=p*0.9
print("The total is "+str(p))
a=int(input("Please enter a number:"))
if a%2==0:
    print(str(a)+"為偶數")
else:
    print(str(a)+"為奇數")
r=int(input("三角形邊長a ："))
t=int(input("三角形邊長b ："))
y=int(input("三角形邊長b ："))
if (r+t>y and r+y>t and t+y>r):
    print("可構成三角形")
else:
    print("No way")

weight=int(input("Please enter the weight :"))
if (weight<=5):
    price="郵資為50"
elif (weight<=10):
    price="郵資為70"
elif (weight<=15):
    price="郵資為90"
elif (weight<=20):
    price="郵資為110"
else:
    price="超過20公斤無法寄送"
print(price)

kg =float(input("輸入你的體重辣："))
m=float(input("阿你的身高(m)："))
bmi=kg/(m**2)
if (bmi<18):
    print("紙片人")
elif(bmi<24):
    print("Nice 正常:D")
elif(bmi<27):
    print("有點肉喔")
else:
    print("超胖誒 🈹️")

money=int(input("金額："))
if money>=100000:
    money=money*0.8
elif money>=50000:
    money=money*0.85
elif money>=30000:
    money=money*0.90
elif money>=10000:
    money=money*0.95
print(str(money)+"元")

a1=int(input("a:"))
a2=int(input("b:"))
a3=int(input("c:"))

if a1>a2:
    if a1>a3:
        print("最大的值為："+str(a1))
    else:
        print("最大的值為："+str(a3))
elif a2>a3:
    print("最大的值為："+str(a2))
else:
    print("最大的值為："+str(a3))

month=int(input("輸入月份："))
if month<=3:
    print("Spring")
elif month<=6:
    print("Summer")
elif month<=9:
    print("Autumn")
elif month<=12:
    print("Winter")

gg=int(input("金額："))
if gg>=2000000:
    result=gg*0.3
elif gg>=1000000:
    result=gg*0.21
elif gg>=600000:
    result=gg*0.13
elif gg>=300000:
    result=gg*0.06
else:
    result="0"
print("付稅金額:"+str(result))
'''
x=int(input("輸入x座標："))
y=int(input("輸入y座標："))
if (x<0):
    if (y<0):
        print("第三象限")
    elif(y>0):
        print("第二象限")
    elif(y==0):
        print("On y line")
elif (x>0):
    if (y>0):
        print("第一象限")
    elif(y<0):
        print("第四象限")
    elif(y==0):
        print("On y line")
elif (x==0):
        print("On x line")




