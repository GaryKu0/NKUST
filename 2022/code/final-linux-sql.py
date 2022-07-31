from numpy import append
import pymysql
import subprocess
conn=pymysql.connect(host='localhost',user='su',passwd='su',db='UWU',port=3306,charset='utf8')
cursor=conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT * FROM `loginaccount`")
a=cursor.fetchall()
password=[]
for i in range(len(a)):
    proc=subprocess.Popen(['adduser','--gid','1001',"{}".format(a[i]['account'])],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
    ) 
    c="{}\n{}\n\n\n\n\n\nY\n".format(a[i]['password'],a[i]['password'])
    #convert c to bytes
    c=bytes(c, 'utf-8')
    out,err=proc.communicate(c)
    proc.wait()
    print(a[i]['account'])
    print(a[i]['password'])
    print(out,err)