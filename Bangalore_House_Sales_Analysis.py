#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data=pd.read_csv('C:/Bengaluru_House_Data.csv')


# In[4]:


data


# In[5]:


data.shape


# In[6]:


data.head(10)


# In[7]:


data.info()


# In[8]:


data.tail(10)


# In[9]:


#describe() method return description of the dataframe(i.e mean, count etc)
data.describe()


# In[11]:


#using describe() for specific column
data[['bath','price']].describe()


# In[12]:


data['area_type'].unique()


# In[13]:


data['location'].value_counts()


# In[14]:


data['location'].unique()


# In[15]:


#Grouping of House sales data


# In[18]:


#Grouping area_type with sum of price of the flat
data.groupby('area_type',as_index=False)['price'].sum(10)


# In[22]:


#Grouping location with sum of price of the flat
data.groupby('location',as_index=False)['price'].sum(10).sort_values('price',ascending=False).head(10)


# In[24]:


data.groupby(['location','size'],as_index=False)['price'].sum(10).sort_values('price',ascending=False).head(10)


# In[25]:


#Filteration 


# In[31]:


#Filteration of location which as more total price than 1000 lakh
price_location=data.groupby('location',as_index=False)['price'].sum(10).sort_values('price',ascending=False)
price_location[price_location['price']>1000]

the above are the location which has total price more than 1000 lakh
# In[34]:


#Filteration of location and size which as more total price than 1000 lakh
size_price=data.groupby(['location','size'],as_index=False)['price'].sum(10).sort_values('price',ascending=False)
size_price[size_price['price']>1000]

the above data is the location and size which has more total price than 1000 lakh
# In[37]:


#finding null values
data.isnull().sum()


# In[38]:


#removing null Values
data.fillna(method='pad',inplace=True)


# In[40]:


data.isnull().sum()


# # Exploratory data Analysis

# In[43]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[44]:


# Area_type


# In[45]:


sns.countplot(data=data,x='area_type')


# In[49]:


ok=data.groupby('area_type',as_index=False)['price']


# In[51]:


sns.barplot(data=data,x='area_type',y='price')

from the above graph it is shown that plot area has the highest price in total
# In[53]:


# location


# In[54]:


sns.countplot(data=data,x='location')


# In[70]:


price_location=data.groupby('location',as_index=False)['price'].sum(10).sort_values('price',ascending=False).head(5)


# In[71]:


sns.barplot(data=price_location,x='location',y='price')

from the above graph it is shown that whitefield has the highest total price
# In[57]:


#society


# In[63]:


society=data.groupby('society',as_index=False)['price'].sum().sort_values('price',ascending=False).head(5)


# In[64]:


sns.barplot(data=society,x='society',y='price')

from the above graph it is shown that pheston society has the highest price 
# In[66]:


data.columns


# In[67]:


#size


# In[68]:


my=data.groupby('size',as_index=False)['price'].sum().sort_values('price',ascending=False).head(5)


# In[69]:


sns.barplot(data=my,x='size',y='price')

from the above graph it is shown that 3 BHK has the highest total price
# # Conclusion
Flat of 3 BHk from pheston society which is situated in whitefield has the highest total price in Bangalore.