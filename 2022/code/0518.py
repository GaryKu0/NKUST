
import json
f=open('C:/Users/admin/OneDrive - sudevtw/桌面/VsCode/NKUST/response.json','r',encoding='utf-8')
data= json.load(f)
f.close()
import pandas as pd
df = pd.read_json (r'C:/Users/admin/OneDrive - sudevtw/桌面/VsCode/NKUST/response.json')
df.to_csv (r'C:/Users/admin/OneDrive - sudevtw/桌面/VsCode/NKUST/response1.csv', index = None)
#tmp=(data['name_servers']) 
#headerValue=""
#bodyValue=""
#tmp1=""
#for i in data:
#    headerValue+=i+","
#    if (isinstance(data[i], list)) :
#        for s in data[i]:
#            tmp1+=s+"&"
#        tmp1=tmp1[:-1]
#    elif (data[i] is None) :
#           tmp1+="null"
#    else:
#        tmp1=data[i]
#    bodyValue+=tmp1+","
#    tmp1=""
#print(headerValue)
#print(bodyValue)
#create a new csv file and write headervalue and bodyvalue to it
#w=open("result.csv","w")
#w.write(headerValue+"\n")
#w.write(bodyValue)
#w.close()
    
        