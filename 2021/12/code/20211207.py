i = 1
data = {}
while i <= 3:
    name = input("請輸入第"+str(i)+"同學的名字:")
    grade = int(input("請輸入第"+str(i)+"同學成績:"))
    data.update({name: grade})
    i=i+1
highest_grade=max(data.values())
name = list(data.keys())[list(data.values()).index(highest_grade)]
print("highest grade: "+str(highest_grade)+"highest name: "+name))