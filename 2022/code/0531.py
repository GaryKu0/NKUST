import pandas as pd
import json
f=open('C:\\Users\\admin\\OneDrive - sudevtw\\桌面\\VsCode\\NKUST\\2022\\code\\uu.json','r',encoding='utf-8')
data=json.load(f)
f.close()
tmp=pd.DataFrame(data)
tmp=tmp.drop(['sno','tot','sbi','mday','lat','lng','bemp','act','srcUpdateTime','updateTime','infoTime','infoDate','sareaen',"snaen","aren"],axis=1)
#count every sarea
tmp1=tmp.groupby(['sarea'])['sarea'].count()
print(tmp1.sort_values())
