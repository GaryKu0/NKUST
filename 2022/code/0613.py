import pymysql
import json
conn=pymysql.connect(host='localhost',user='root',passwd='',db='nkust',port=3306,charset='utf8')
cursor=conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("INSERT INTO `student-list`(`id`, `name`, `tel`, `addr`) VALUES ('12','蘋果派','0800000123','moon')")
cursor.execute("SELECT * FROM `student-list`")
a=cursor.fetchall()
for i in a:
    print(i)

data=[]
for i in a:
    data.append(i)
tmp=json.dumps(data,ensure_ascii=False,indent=4)
print(tmp)
