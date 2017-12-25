from pymongo import MongoClient

client = MongoClient('mongodb://m001-sandbox-shard-00-00-rdhhd.mongodb.net:27017,m001-sandbox-shard-00-01-rdhhd.mongodb.net:27017,m001-sandbox-shard-00-02-rdhhd.mongodb.net:27017/test?replicaSet=m001-sandbox-shard-0" --ssl --authenticationDatabase admin - -username m001-student --password m001-mongodb-basics')

client.database_names()
