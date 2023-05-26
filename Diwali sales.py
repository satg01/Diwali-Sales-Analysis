#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[9]:


df=pd.read_csv("C:\Desktop\Data Analyst Project\python & Power BI\Python_Diwali_Sales_Analysis-main\diwalisale.csv",encoding= 'unicode_escape')


# In[10]:


df.shape


# In[11]:


df.head(10)


# In[20]:


df.info()


# In[22]:


df.drop(['unnamed'], axis=1, inplace=True)


# we use drop to delete unrelated data

# In[24]:


df.info()


# In[26]:


pd.isnull(df) #check null values


# In[27]:


df.dropna(inplace=True)


# In[29]:


df.shape


# In[31]:


df['Amount']=df['Amount'].astype('int') #change data type from current to integer


# In[32]:


df['Amount'].dtype


# In[33]:


df.columns


# In[35]:


df.rename(columns={'Occupation':'Service'})


# In[36]:


df.info


# In[37]:


df.columns


# In[39]:


df[['Cust_name','Age','Occupation','Amount']].describe() #describe show only numeric type as we can see cust_name and Occupation


# In[40]:


df.columns


# In[67]:


ax=sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# most of the buyers are female as described  above 

# In[91]:


oc=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[95]:


bx=sns.barplot(x='Occupation' ,y='Amount',data=oc)
plt.xticks(rotation=90)

#for bars in bx.containers: bx.bar_label(bars)
plt.show


# most buyrs are from It Sector,Healthvare and Aviation respectively

# In[72]:


df.columns


# In[114]:


ax=sns.countplot(data=df,x='Age Group',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[112]:


cx=df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=cx, x='Age Group',y='Amount')


# In[119]:


dx=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)


# In[143]:


sns.set(rc={'figure.figsize':(13,5)})
plt.xticks(rotation=40)
sns.barplot(data=dx , x='State',y='Orders')
#top 10 states based on orders made  by tyhe customrs 


# from the above graph we can see that most of the oreders from uttarpradesh,Maharashtra and Karnataka respectively 

# In[134]:


ex=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(x='State',y='Amount',data=ex)
plt.xticks(rotation=40)
plt.show
#top 10 states with moat spent amount by customers 


# In[157]:


ex=sns.countplot(data=df, x='Marital_Status')
sns.set(rc={'figure.figsize':(5,3)})
for bars in ex.containers:
    ex.bar_label(bars)


# In[177]:


mar= df.groupby (['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(5,4)})
sns.barplot(data=mar, x = 'Marital_Status', y='Amount',hue='Gender')


# from above graph we can see that most of the buyers are unmarried womens

# In[178]:


df.columns


# # Product_category

# In[187]:


cx=sns.countplot(data=df,x='Product_Category')
sns.set(rc={'figure.figsize':(15,5)})
for bars in cx.containers:
    cx.bar_label(bars)
plt.xticks(rotation=80)


# In[189]:


dx=df.groupby(['Product_Category'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
sns.barplot(data=dx,x='Product_Category',y='Orders')
plt.xticks(rotation=90)


# In[197]:


px=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.barplot(x='Product_Category',y='Amount',data=px)

plt.xticks(rotation=70)


# In[202]:


sells=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(12,5)})
sns.barplot(data=sells, x='Product_ID', y='Orders')


# In[203]:


#top 10 selling product


# # conclusion:
#   
#   "single women age group 25-35 years from uttarpradesh,Maharashtra  and Karnataka working in IT sector ,Healthcare and Aviation 
#   are more likely to buy Products from food,clothing and electronic categories
