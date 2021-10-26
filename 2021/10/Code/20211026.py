'''
temp=float(input("請輸入溫度："))
if temp <36:
    print("體溫過低")
elif temp <38:
    print("體溫正常")
elif temp<39:
    print("體溫有點燒")
else :
    print("你要煮熟了")
year=int(input("輸入年份："))
if year%4==0:
    if year%100==0:
        if year%400==0:
            res="是閏年"
        else:
            res="不是閏年"
    else:
        res="是閏年"
else:
    res="是閏年"
print(str(year)+" "+str(res))

score = float (input("Type score (1-100)"))
if score <0 or score>100:
    print("error!")
else:
    if 90<=score:
        print("A")
    else:
        if 80<=score:
            print("B")
        else:
            if 70<=score:
                print("C")
            else:
                if 60<=score:
                    print("D")
                else:
                    print("E")

gender =input("Your Gender: (m/f)")
kg =float(input("輸入你的體重辣："))
m=float(input("阿你的身高(m)："))
bmi=kg/(m**2)
print("Your BMI: "+str(bmi))
if gender=="f":
    if bmi>=26:
        print("超胖誒 🈹️")
    else:
        print("Normal")
else:
    if bmi>=31:
        print("超胖誒 🈹️")
    else:
        print("Normal")
if (bmi<18):
    print("紙片人")
elif(bmi<24):
    print("Nice 正常:D")
elif(bmi<27):
    print("有點肉喔")
else:
    print("超胖誒 🈹️")

mid=int(input("期中考成績："))
final=int(input("期末考成績："))
if (mid <=100 and final <=100):
    result=mid*0.4+final*0.6
    #Copy
    if 90<=result:
        print(str(result)+" A")
    else:
        if 80<=result:
            print(str(result)+" B")
        else:
            if 70<=result:
                print(str(result)+" C")
            else:
                if 60<=result:
                    print(str(result)+" D")
                else:
                    print(str(result)+" E")
else:
    print("不要給我亂打 ^^")

x = float(input("輸入x座標："))
y = float(input("輸入y座標："))
if (x < 0):
    if (y < 0):
        print("第三象限")
    elif(y > 0):
        print("第二象限")
    elif(y == 0):
        print("On y line")
elif (x > 0):
    if (y > 0):
        print("第一象限")
    elif(y < 0):
        print("第四象限")
    elif(y == 0):
        print("On y line")
elif (x == 0):
    if (y == 0):
        print("原點")
    else:
        print("On x line")
'''
from typing import SupportsAbs


CarType=input("Type your Car Type (B or C):")
Speed=float(input("超速幾公里?"))
B=[1200,1400,1600,8000,12000,24000]
C=[1600,1800,2000,8000,12000,24000]
if CarType=="b":
    if Speed<20: 
        print("罰"+str(B[0]))
    elif Speed<40:
        print("罰"+str(B[1]))
    elif Speed<60:
        print("罰"+str(B[2]))
    elif Speed<80:
        print("罰"+str(B[3]))
    elif Speed<100:
        print("罰"+str(B[4]))
    elif Speed >=100:
        print("罰"+str(B[5]))   
elif CarType=="c":
    if Speed<20: 
        print("罰"+str(C[0]))
    elif Speed<40:
        print("罰"+str(C[1]))
    elif Speed<60:
        print("罰"+str(C[2]))
    elif Speed<80:
        print("罰"+str(C[3]))
    elif Speed<100:
        print("罰"+str(C[4]))
    elif Speed >=100:
        print("罰"+str(C[5])) 
else:
    print("車子種類好特別 沒看過")



