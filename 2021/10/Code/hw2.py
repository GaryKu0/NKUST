"""
c=int(input("請輸入座號:"))
d=0
b=0
while b<c:
    b=b+5
    d=d+1

print("你是第"+str(d)+"組")
"""
soda=int(input("要買幾罐?"))
da=int(soda/12)
left=soda%12
re=da*200+left*20
print("你買了"+str(da)+"打又"+str(left)+"罐請付"+str(re)+"元")