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
'''
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

