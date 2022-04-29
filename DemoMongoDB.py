# Demo MongoDB
import pymongo

# Connect
connectstring = "mongodb+srv://hellstern:password@cluster0.huvwp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(connectstring)

# Create
mydb = myclient["mydatabase2"]
mycol = mydb["customers2"]

# Create a new document
#mycol.insert_one({"-id":101, "companyname":"Kea", "contact":"Tue Hellstern"})
#mycol.insert_one({"-id":102, "companyname":"CPH Business", "contact":"Ole Hansen"})
#mycol.insert_one({"-id":103, "companyname":"ITU", "contact":"Peter Jensen"})
#mycol.insert_one({"-id":104, "companyname":"Somthing", "contact":"Ole Rasmussen", "contry":"UK"})

# Find/Show/print
# Find all
#for x in mycol.find():
#    print(x)

# "Select" columns

# Exclude id and lastname
#for x in mycol.find({},{ "-id": 0, "companyname": 0 }):
#    print(x)

# Update One - Only fist one
myquery = { "companyname": "Kea" }
newvalues = { "$set": { "companyname": "New Kea" } }
mycol.update_one(myquery, newvalues)

#Drop/Delete colection
#mycol.drop()
















