import pymongo
import ssl

client = pymongo.MongoClient("mongodb+srv://pp2:pp2password@cluster0-r3cj5.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs = ssl.CERT_NONE)

mydb = client['mydatabase']

print(client.list_database_names())

mycol = mydb['students']

print(mydb.list_collection_names())

mydict = {'name': 'Arystan', 'gpa': '3.5'}

x = mycol.insert_one(mydict)

print(x.inserted_id)

mylist = [
  { "name": "Amy", "gpa": "2.3"},
  { "name": "Hannah", "gpa": "1.7"},
  { "name": "Michael", "gpa": "4.0"},
  { "name": "Sandy", "gpa": "3.2"},
  { "name": "Betty", "gpa": "2.1"},
  { "name": "Richard", "gpa": "1.5"},
  { "name": "Susan", "gpa": "3.4"},
  { "name": "Vicky", "gpa": "2.8"},
  { "name": "Ben", "gpa": "3.8"},
  { "name": "William", "gpa": "2.5"},
  { "name": "Chuck", "gpa": "3.1"},
  { "name": "Viola", "gpa": "2.2"}  
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)

x = mycol.find_one()
print(x)

for x in mycol.find():
   print(x)

for x in mycol.find({},{ "name": 1 }):
   print(x)

myquery = {"gpa": "3.1"}
mydoc = mycol.find(myquery)
for x in mydoc:
   print (x)

myquery = {"gpa": {"$gt":"2.0"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

mydoc = mycol.find().sort("name")
for x in mydoc:
    print(x)

mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)

myquery = {"name": "Arystan"}
mycol.delete_one(myquery)

myquery = { "gpa": {"$gt": "3.0"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, "documents deleted.")

x = mycol.delete_many({})
print(x.deleted_count, "documents deleted.")

#mycol.drop()

myquery = {"name": "Amy"}
new_val = {"$set": {"name": "Andy"}}

mycol.update_one(myquery, new_val)

for x in mycol.find():
    print(x)

myquery = {"gpa": {"$gt": "2.0"}}
new_val = {"$set": {"gpa": "4.0"}}

x = mycol.update_many(myquery,new_val)

print(x.modified_count, "uptated docs")

myresult = mycol.find().limit(2)
for x in myresult:
    print(x)