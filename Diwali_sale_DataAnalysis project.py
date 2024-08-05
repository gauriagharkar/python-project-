#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import python libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[5]:


#import csv file
df = pd.read_csv("C:/Users/LENOVO/Desktop/Python_Diwali_Sales_Analysis/Diwali Sales Data.csv",encoding='unicode_escape')


# In[6]:


df.shape


# In[7]:


df.head()


# In[8]:


df.head(20)


# In[9]:


df.info()


# In[12]:


#drop unrelated/blank columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[14]:


df.info()


# In[15]:


# check for null values
pd.isnull(df).sum()


# In[16]:


# drop null values 
df.dropna(inplace=True)


# In[17]:


# change data type 
df['Amount'] = df['Amount'].astype('int')


# In[18]:


df['Amount'].dtypes


# In[20]:


df.columns


# In[22]:


# rename column
df.rename(columns={'Marital_Status':'Shaadi'})


# In[23]:


df.rename(columns={'Age Group':'GroupAge'})


# In[25]:


#describe() method return description of the data in the dataframe(i.e count,mean,std,etc)
df.describe()


# In[27]:


#use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# In[32]:


#EXPLORATORY DATA ANALYSIS
#Gender
#plotting a bar chart for gender and its'scount
ax =sns.countplot(x ='Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[33]:


# plotting a bar  chart for gender vs total amount
sales_gen= df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data= sales_gen)


# # AGE

# In[34]:


ax = sns.countplot(data = df,x = 'Age Group',hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[35]:


# total amount vs age group
sales_age = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x = 'Age Group',y = 'Amount',data = sales_age)


# # from above we can see that most of the buyers are of age group between 26-35 female

# # state

# In[43]:


# total number of order from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[44]:


#total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# # from above graphs we can  see that most of the orders of the orders& total sale/amount are from uttarpradesh,maharashtra and karnataka

# # Marital Status

# In[45]:


ax = sns.countplot(data = df, x='Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bar in ax.containers:
    ax.bar_label(bar)


# In[50]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# # From Above graphs we can see that most of the buyers are married (Women)and they have high purchasing power
# 

# # OCCUUPATION

# In[52]:


sns.set(rc={'figure.figsize':(29,8)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[53]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# # PRODUCT CATEGORY

# In[55]:


sns.set(rc={'figure.figsize':(28,9)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[56]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Zone')

for bars in ax.containers:
    ax.bar_label(bars)


# ###### from above graphs we can see that most of the sold product are from food,clothing and Electronics category

# In[61]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[62]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # CONCLUSION:

# ###### Married women age group 26-35 yrs from up,Maharastra and karnataka working in IT,Healthcare and Aviation are more likely to buy products from food,clothing and Electronics category
# 

# In[ ]:




