list1 = range(5)
print(list(list1))
list2 = range(0, 10, 3)
print(list(list2))
list3 = range(1, 10, 2)
print(list(list3))
list4 = range(10, 0, -2)
print(list(list4))

lang1 = {"早安": "Good Morning", "午安": "Good Afternoon", "晚安": "Good Evening"}
if "早安" in lang1:
    print("早安的英文是"+lang1["早安"])
else:
    print("查無此字彙")

numm = int(input("請輸入一個數字："))
for i in range(0, numm):
    if (i % 5 == 0):
        continue
    print(i, end=",")
