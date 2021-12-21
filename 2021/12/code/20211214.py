

list1 = ["台北市","高雄市","屏東縣","台東縣"]
input_values = input("請輸入要查詢得縣市名稱:")
if input_values in list1:
    print("此縣市在台灣")
else:
    print (input_values,"不在清單中")


pm25_dict = {"台北市":"9","高雄市":"5"}
input_values = input("請輸入要查詢得縣市名稱:")
if input_values in pm25_dict:
    print(input_values,"今天pm2.5值為",pm25_dict[input_values])
    
a={"鼠":"親切和藹","牛":"保守努力","虎":"熱情大膽","兔":"溫柔仁慈"}
#use a's items to convert to a list
list2 = list(a.items())
for name,value in list2:
    print("生肖屬",name,"性格特徵為",value)

Whole_class=set(['John', 'Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
Eng_pass=set(['John','Mary','Claire','Fiona','Ben','Bill'])
Math_pass=set(['Mary','Fiona','Claire','Eva','Ben'])
print("全班同學通過的學生有:",Whole_class.intersection(Eng_pass,Math_pass))
print("全班同學未通過數學的學生有:",Whole_class.difference(Math_pass))
print("全班同學英文通過數學沒通過的學生有:",Eng_pass.difference(Math_pass))
