"""
s1=int(input("你的薪水: "))
s2=int(input("你的工作獎金: "))
s3=int(input("你的加班費: "))
final =s1+s2+s3
print("你能領到"+str(final)+"元")
"""
YN="y"
result=""
while YN=="y":
    a1=str(input("姓名:"))
    a2=str(input("座號:"))
    a3=str(input("國文:"))
    a4=str(input("數學:"))
    a5=str(input("英文:"))
    YN=input("是否還有其他人? (y or n)")
    if YN=="y":
        result=result+"%3s%3s   %3s   %3s   %3s\n"%(a1,a2,a3,a4,a5)
    else:
        pass
print ("姓名  座號  國文  數學  英文")
print("%3s%3s   %3s   %3s   %3s"%(a1,a2,a3,a4,a5))
print (result)

NY="y"
result2=""
while NY=="y":
    b1=str(input("年度:"))
    b2=str(input("所得稅:"))
    b3=str(input("營業稅:"))
    b4=str(input("證交稅:"))
    NY=input("是否還有其他資料? (y or n)")
    if NY=="y":
        result2=result2+"%4s  %5s   %5s  %5s\n"%(b1,b2,b3,b4)
    else:
        pass
print ("年度  所得稅  營業稅  證交稅")
print("%4s  %5s   %5s  %5s"%(b1,b2,b3,b4))
print (result2)






