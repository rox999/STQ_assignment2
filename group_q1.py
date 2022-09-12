import datetime
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["smartshark"]
my_project_collection = mydb["project"]
my_commit_collection = mydb["commit_with_project_info"]

start = datetime.datetime(2017, 2, 20)
end = datetime.datetime(2017, 2, 22, 23, 59, 59)

mydoc = my_commit_collection.find({'$and': [{'project_name_info.name': 'kafka'}, {'committer_date': {'$gte': start, '$lt': end}}]})

kafka_commit_list = []

for x in mydoc:
    kafka_commit_list.append(x['_id'])
print(len(kafka_commit_list))
print(kafka_commit_list)