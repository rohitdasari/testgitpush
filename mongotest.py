import pymongo

client = pymongo.MongoClient("mongodb+srv://rohit:RohitDasaRi99@cluster1.xvzbrbd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name":"Rohit",
    "email":"dasarirohit123265@gmail.com",
    "surname":'Dasari'
}

db1 = client['mongotest']
col1 = db1['test']
col1.insert_one(d)