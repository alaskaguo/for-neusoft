
# coding: utf-8

# In[227]:


import pandas as pd
import os
from datetime import datetime
import time
from dateutil.parser import parse


# In[228]:


path = r"D:\20200720"
os.chdir(path)
filelist = os.listdir(path)


# In[229]:


## check the dimension of all df
for file in filelist:
    df = pd.read_excel(file)
    print(file,df.shape)


# In[230]:


colnames = pd.read_excel(r"D:\myresearch\data\columns_1.xlsx").iloc[:,0]


# In[231]:


## 年龄列去掉文字，一岁一下按0岁处理
def intage(age):
    ''' convert age string to age int'''
    agenum = []
    if ('岁' in age) == False:
        currentage = 0
    else:
        for letter in age:
            if letter == '岁':
                break;
            else:
                agenum.append(letter)
        currentage = int(''.join(agenum))         
    return currentage;


# In[232]:


df_total = pd.DataFrame()


# In[233]:


for file in filelist:
    df = pd.read_excel(file,header=None)

    df.columns = colnames

    ## 取得文件建立时间，单列一列,实际命令是getmtime：修改时间
    set_time = time.ctime(os.path.getmtime(file))
    print(set_time)
    df["set_time"] = parse(set_time)
    
    df["currentageint"] = df["currentage"].apply(intage)

    df["recordageint"] = round(df["currentageint"] -  (df["set_time"] - df["record_time"]).apply(lambda x:x.days)/365)

    colreserve = ['department', 'doctor_name', 'patient_name',
           'currentage', 'patient_id', 'chief_complaint', 'present_illness',
           'past_illness', 'personal_history', 'allergic', 'physical_exam',
           'entrust', 'issignature', 'record_time',
           'diagnosis','recordageint']

    df = df[colreserve]
    df_total = df_total.append(df)


# In[ ]:


set_time


# In[ ]:


df.shape


# In[ ]:


df_total.shape


# In[234]:


df_total.to_csv(r"D:\myresearch\data\data_total.csv",index=0,encoding="utf-8")

