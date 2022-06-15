import pandas as pd
from urllib import response
import requests
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
data_url="https://quality.data.gov.tw/dq_download_json.php?nid=148639&md5_url=7721901919db2cfc1abe4ea3350819e7"
#get data from data_url
data=requests.get(data_url)
plt.rc('axes',unicode_minus=False)
#convert json to pandas dataframe

tmp=pd.DataFrame(data.json())
print(tmp)
#make chart with pandas
chart=tmp.plot(x ='屆別', y='男性', kind = 'scatter', color='blue', label='男性')
plt.show()



