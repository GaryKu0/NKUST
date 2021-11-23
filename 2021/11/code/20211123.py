'''
total=i=1
n=int(input("正整數值："))
while i<=n:
    total*=i
    i+=1
print("%d!=%d" % (n,total))

for i in range(1,n+1):
    total*=i 
print("%d!=%d" % (n,total))
'''
import math
# 要求輸入三個值 判別是什麼三角形
l1 = float(input("請輸入最長邊長："))
l2 = float(input("請輸入最短邊長："))
l3 = float(input("請輸入第三個邊長："))
# 判斷是否為三角形
l3d = math.degrees(math.acos((l1**2+l2**2-l3**2)/(2*l1*l2)))
l1d = math.degrees(math.acos((l2**2+l3**2-l1**2)/(2*l2*l3)))
l2d = math.degrees(math.acos((l3**2+l1**2-l2**2)/(2*l3*l1)))
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    if l1 == l2 == l3:
        answer = "正三角形"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        if l3d > 90 or l2d > 90 or l1d > 90:
            answer = "等腰鈍角三角形"
        elif l3d < 90 and l2d < 90 and l1d < 90:
            answer = "等腰銳角三角形"
        else:
            answer = "等腰直角三角形"
    elif l1**2+l2**2 == l3**2 or l1**2+l3**2 == l2**2 or l2**2+l3**2 == l1**2:
        answer = "直角三角形"
    elif l1**2+l2**2-l3**2/2*l1*l2 > 90 or l2**2+l3**2-l1**2/2*l2*l3 > 90 or l3**2+l1**2-l2**2/2*l3*l1 > 90:
        answer = "鈍角三角形"
    elif l1**2+l2**2-l3**2/2*l1*l2 < 90 or l2**2+l3**2-l1**2/2*l2*l3 < 90 or l3**2+l1**2-l2**2/2*l3*l1 < 90:
        answer = "銳角三角形"
    print(answer)
    print("三個角度為：%d,%d,%d" % (l1d, l2d, l3d))
else:
    print("無法構成三角形")


'''
#ask user to input a number
number=int(input("Input a number"))
i=1
b=1
while b<number:
    b*=i
    i+=1
print("%d 階乘為 %d大於"%(i-1,b,number))

numm = int(input("請輸入一個數字："))
# 計算1到numm的偶數總和
a2 = 0
num1 = numm
while numm > 0:
    if numm % 2 == 0:
        a2 += numm
        numm -= 2
    else:
        numm -= 1
        print(numm)
print("1到%d的偶數總和為%d" % (num1, a2))
a1 = 0
numm = num1
# 計算1到numm的奇數總和
while numm > 0:
    if numm % 2 == 1:
        a1 += numm
        numm -= 2
    else:
        numm -= 1
print("1到%d的奇數總和為%d" % (num1, a1))
numm = num1
a37 = 0
# 計算1到numm的3和7倍數的總和
while numm >= 0:
    if numm % 3 == 0 or numm % 7 == 0:
        a37 += numm
    numm -= 1
print("1到%d的3和7倍數的總和為%d" % (num1, a37))
#比較a2,a1,a37的大小
if a2>a1 and a2>a37:
    print("偶數總和")
elif a1>a2 and a1>a37:
    print("奇數總和")
else:
    print("3和7倍數的總和最大")  
'''
'''
intnum = int(input("請輸入一個數字："))
#計算intnum的因數
for i in range(1,intnum+1):
    if intnum%i==0:
        print(i,end=",")
#判斷intnum是否為質數
c=2
while c < intnum:
    if intnum % c == 0:
        print('不是質數')
        break
    c += 1
if c == intnum:
    print('是質數')
'''
