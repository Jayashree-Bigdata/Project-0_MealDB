# Project-0_MealDB

# Use MongoDB for NoSQL
1. Meal database actually contains the different types of country foods
2. Meal database-(MongoDB, python)

# import required modules
import warnings
from pymongo import MongoClient
warnings.filterwarnings('ignore')

# connection to the client
client = MongoClient('localhost',27017)

# Mongodb commands
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

# to insert_many()
info_data.insert_many(manyRecords)

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

