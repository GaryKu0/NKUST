x=0;y=1
age,name=18,"NKUST_IC"
msg="""
a
b
c
d
e
f
"""
print(x,age,name)
print(msg)

print(100,"早安",True)

print(str(100)+"早安"+str(True))

print(100,"Hello",True,sep = " # ",end=".\n")

print("%s的成績是%d分"%("班代",90))

print("%9s's score is%3d"%("PineApple",98))

print("%12s's score is%-3d"%("PineApple",98))

print("My bmi is: %.2f"%(15.578))

print ("{1}'s score is{0}".format(87,"Pigeon"))

print("{0:5s}'s score is {1:.2f}".format("BOO",67))

name1="Griffindor"
score="5"
print(f"{name1}!plus {score} point!")

#這個題目用等寬字體很有優勢...
print("{0:4s}{1:4s}{2:3s}{3:3s}{4:3s}".format("姓名","座號","國文","數學","英文"))
print("%3s%4s %4s %4s  %4s "%("林大明","1","100","87","79"))
print("%3s%4s %4s %4s  %4s "%("陳阿中","2","74","88","100"))
print("%3s%4s %4s %4s  %4s "%("張小英","11","82","65","8"))

print("\n")

print("{0:4s}{1:4s}{2:4s}{3:4s}".format("年度","所得稅","營業稅","證交稅"))
print("%3s  %5s  %5s  %5s "%("2017","98.34","90.20","104.79"))
print("%3s  %5s  %5s  %5s "%("2016","83.00","110.50","82.45"))
print("%3s  %5s  %5s  %5s "%("2015","98.00","79.32","102.00"))
