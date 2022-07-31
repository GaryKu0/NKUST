from cProfile import label
import pandas as pd
from urllib import response
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rcParams
import matplotlib as mpl

#-------------------------字體設定----------------------------------------
rcParams['font.family'] = 'SDK_SC_Web'
gsfont = {'fontname':'SDK_SC_Web'}
#-------------------------字體設定----------------------------------------

#-------------------------讀取json檔案------------------------------------
#data_url="https://sususu.su/python/salary.json"
#get data from data_url
#data=requests.get(data_url)#
f=open("C:\\Users\\admin\\Downloads\\csvjson.json","r",encoding='utf-8')
data=json.load(f)
f.close()
#-------------------------讀取json檔案------------------------------------
##tmp=pd.DataFrame(data.json())
tmp=pd.DataFrame(data)
print(tmp)
#-------------------------各個職業的占比-----------------------------------
job_title=tmp.groupby(['job_title'])['job_title'].count()
del_list=[]
other=0
for i in job_title.index:
    if job_title[i]<10:
        del_list.append(i)
        other+=1
for i in del_list:
    job_title.drop(i,inplace=True)
#job_title add other
job_title.loc['Other']=other
job_title=job_title.sort_values(ascending=False)
chart=job_title.plot(kind='pie',figsize=(10,14),autopct='%1.1f%%',fontsize=20)
plt.title('各職業占比',fontsize=30,**gsfont)
plt.show()
plt.clf()
#-------------------------各個職業的占比--------------------------------------
#
#-------------------------美國工作薪資區間-----------------------------------
Country='CA'#填入你要查詢的國家
US_SAL=tmp
US_SAL.drop(['work_year','experience_level','employment_type','salary_currency','salary','remote_ratio','employee_residence','company_size'],axis=1,inplace=True)
#get all value in company location contain "US"
US_SAL=US_SAL[US_SAL['company_location'].str.contains('CA')]
US_SAL=US_SAL.sort_values(by='salary_in_usd',ascending=True)
US_SAL.drop(US_SAL.columns[0],axis=1,inplace=True)
#UNDER 100k
US_SAL_100k=US_SAL[US_SAL['salary_in_usd']<100001].shape[0]#UNDER 250k
US_SAL_250k=US_SAL[US_SAL['salary_in_usd']<250001].shape[0]-US_SAL_100k#UNDER 450k
US_SAL_450k=US_SAL[US_SAL['salary_in_usd']<450001].shape[0]-US_SAL[US_SAL['salary_in_usd']<250001].shape[0]#UNDER 600k
US_SAL_600k=US_SAL[US_SAL['salary_in_usd']<600001].shape[0]-US_SAL[US_SAL['salary_in_usd']<450001].shape[0]  
#
#US_SAL_100k=US_SAL[US_SAL['salary_in_usd']<25001].shape[0]#UNDER 25k
#US_SAL_250k=US_SAL[US_SAL['salary_in_usd']<50001].shape[0]-US_SAL_100k#UNDER 50k
#US_SAL_450k=US_SAL[US_SAL['salary_in_usd']<75001].shape[0]-US_SAL[US_SAL['salary_in_usd']<50001].shape[0]#UNDER 50k
#US_SAL_600k=US_SAL[US_SAL['salary_in_usd']<100001].shape[0]-US_SAL[US_SAL['salary_in_usd']<75001].shape[0]      

#made a pie chart
labels = ['UNDER 100k','100k~250k','250k~450k','\n\n450k~600k ']
#labels=['UNDER 25k','25k~50k','50k~75k','75k~100k']
value=[US_SAL_100k,US_SAL_250k,US_SAL_450k,US_SAL_600k]
plt.pie(value,labels=labels,shadow=True,startangle=120)
plt.title('加拿大工作薪資區間',fontsize=30,**gsfont)
#plt.show()
plt.clf()
# -------------------------美國工作薪資區間-----------------------------------
#print(tmp)

#------------------------job_title=Data Scientisit EveryCountry people
job='Data Science Manager'
jobCount=tmp
jobCount=jobCount[jobCount['job_title'].str.contains(job)]
#count every comapany_location
jobCount=jobCount.groupby(['company_location'])['company_location'].count()
del_list=[]
other=0
#----丟棄10位以下的----
#for i in jobCount.index:
#    if jobCount[i]<10:
#        del_list.append(i)
#        other+=1
#for i in del_list:
#    jobCount.drop(i,inplace=True)
#job_title add other
#jobCount.loc['Other']=other
chart=jobCount.plot(kind='pie',figsize=(10,14),autopct='%1.1f%%',fontsize=20)
plt.title('{} 各國公司占比'.format(job),fontsize=30,**gsfont)
#plt.show()
plt.clf()