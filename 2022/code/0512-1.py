from cgitb import reset
import readline
from tokenize import group

class studentscore:
    def __init__(self,subject,score):
        self.subject=subject
        self.score=score
list=[]
f=open('C:/Users/admin/OneDrive - sudevtw/文件/example0512.csv')
result=f.readlines()
for i in result:
    tmp=i.split(",")
    subject=tmp[0]
    score=tmp[1].split('\n')[0]
    p1=studentscore(subject,int(score))
    list.append(p1)
print(list)
f.close
    