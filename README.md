# Project-0_MealDB

# Use MongoDB for NoSQL
1. Meal database actually contains the different types of country foods
2. Meal database-(MongoDB, python)

# import some of the libraries we are going to use
Here we are quering a MongoDB database using Pymongo 
Firstly we insert the data into the database

import warnings
from pymongo import MongoClient
warnings.filterwarnings('ignore')

# connection to the  Mongo client
client = MongoClient('localhost',27017)

# get the database
database = client["MealDB"]

# create collection
info_data = database["collection"]

we use the data from a meal delivery company that operates in multiple places. 
Here MealDB contains
- meal_id
- category
- cuisine

# Mongodb commands
# to insert_many()

inserting data 

manyRecords = [
    {"meal_id":2700,'category':'hjk'},
    {"meal_id":2701,'category':'jik'}
]
info_data.insert_many(manyRecords)

# to find_one()
info_data.find_one()

find_one() method returns the first occurence in the selection

# to find_all()
for i in info_data.find():
    print(i)
    
find() method returns all occurence in the selection

# limit()
for i in info_data.find().limit(5):
    print(i)
    
limit() method takes one parameter, a number defining how many documents to return

# to insert_one() 
info_data.insert_one(record)

# to update_one()
info_data.update_one(myquery,newValues)

# to delete_one() 
info_data.delete_one(record)

# to update_many()
info_data.update_many({'meal_ids': 1}, {'$inc': {'meals_ids': 3}})

# to delete_many()
info_data.delete_many(myquery)

# to count() the records
count = info_data.find().count()
print(count)

# to sort() the records
info_data.find().sort("_id",0)

# to drop()
info_data.drop()

# meal database using mysql
we are going to use the mysql workbench to create the meal database 

# commands which used
Create
Insert
Delete
Select
Alter
Update


