#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
from pymongo import MongoClient
warnings.filterwarnings('ignore')


# In[2]:


client = MongoClient('localhost',27017)


# In[3]:


database = client["MealDB"]


# In[4]:


info_data = database["collection"]


# In[5]:


print(info_data.find_one())


# In[6]:


for i in info_data.find():
    print(i)


# In[7]:


for i in info_data.find().limit(5):
    print(i)


# In[8]:


record = {'meal_id': 2755, 'category': 'Somosa', 'state': 'Indian'}


# In[9]:


info_data.insert_one(record)


# In[10]:


manyRecords = [
    {"meal_id":2700,'category':'hjk'},
    {"meal_id":2701,'category':'jik'}
]


# In[11]:


info_data.insert_many(manyRecords)


# In[12]:


myquery = {"address":"Ap"}
newValues = {"$set":{"address":"nlr"}}


# In[13]:


info_data.update_one(myquery,newValues)


# In[14]:


info_data.delete_one(record)


# In[15]:


info_data.update_many({'meal_ids': 1}, {'$inc': {'meals_ids': 3}})


# In[16]:


info_data.delete_many(myquery)


# In[18]:


count = info_data.find().count()
print(count)


# In[19]:


info_data.find().sort("_id",0)


# In[20]:


info_data.drop()


# In[ ]:




