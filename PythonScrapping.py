#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html')


# In[4]:


print(soup)


# In[6]:


soup.find_all('table')


# In[8]:


workingtable=soup.find_all('table')[0]


# In[9]:


print(workingtable)


# In[11]:


header=workingtable.find_all('th')


# In[12]:


print(header)


# In[17]:


for i in header:
    print(i.text)


# In[20]:


tabletitle=[i.text.strip() for i in header ]


# In[21]:


print(tabletitle)


# In[22]:


import pandas as pd


# In[24]:


df=pd.DataFrame(columns=tabletitle)
df


# In[31]:


data=workingtable.find_all('tr')[1:]


# In[32]:


print(data)


# In[33]:


coldata=[i.text.strip() for i in data]
print(coldata)


# In[44]:


for row in data:
    rowdata=row.find_all('td')
    celldata=[i.text.strip() for i in rowdata]
    del celldata[3]
    del celldata[1]
    length=len(df)
    df.loc[length]=celldata


# In[45]:


df


# In[46]:


df.to_csv(r'C:\Users\Rishav Banerjee\Documents\PythonData\OutputData.csv',index=False)


# In[ ]:




