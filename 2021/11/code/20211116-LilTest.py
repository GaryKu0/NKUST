'''
num = int(input("請輸入ㄧ個數字："))
print(list(range(0, num+1)))

num2 = int(input("請輸入ㄧ個數字："))
num3 = 0
while num2 > 0:
    num3 = num3+num2
    num2 = num2-1
print(str(num3))

StartValue = int(input("輸入加總開始值："))
EndValue = int(input("輸入加總結束值："))
f = int(input("輸入遞增減值："))
AddValue = 0
bb = 0
cc = 0
result = 0
for i in range(StartValue, EndValue, f):
    result = result+i
    print("i為"+str(i)+"加總結果"+str(result))
print("-------------------------------------------------")
while AddValue < EndValue-f:
    bb = StartValue+AddValue
    cc = cc+bb
    print("i為"+str(bb)+"加總結果"+str(cc))
    AddValue = AddValue+f
#輸出99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+"*"+str(i)+"="+str(i*j),end="\t")
    print()
'''
triangle_num = int(input("輸入正整數："))
for i in range(1, triangle_num+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
for i in range(triangle_num+1, 1, -1):
    for j in range(1, i):
        print("*", end="")
    print()
