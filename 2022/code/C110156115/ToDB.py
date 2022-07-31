import pymysql,pandas as pd,requests
conn=pymysql.connect(host='localhost',user='root',passwd='',db='pythonfinaltestdata',port=3306,charset='utf8')
cursor=conn.cursor(pymysql.cursors.DictCursor)
data_url="https://sususu.su/python/salary.json"
data=requests.get(data_url)
data=pd.DataFrame(data.json())
data.drop(data.columns[0],axis=1,inplace=True)
for i in range(len(data)):
    cursor.execute("INSERT INTO `salary`(`work_year`, `experience_level`, `employment_type`, `job_title`, `salary`, `salary_currency`, `salary_in_usd`, `employee_residence`, `remote_ratio`, `company_location`, `company_size`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(data.iloc[i]['work_year'],data.iloc[i]['experience_level'],data.iloc[i]['employment_type'],data.iloc[i]['job_title'],data.iloc[i]['salary'],data.iloc[i]['salary_currency'],data.iloc[i]['salary_in_usd'],data.iloc[i]['employee_residence'],data.iloc[i]['remote_ratio'],data.iloc[i]['company_location'],data.iloc[i]['company_size']))
cursor.execute("SELECT * FROM `salary`")
a=cursor.fetchall()
conn.commit()