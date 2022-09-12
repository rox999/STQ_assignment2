import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["smartshark"]
my_project_collection = mydb["project"]
my_commit_collection =  mydb["commit_with_project_info"]
mydoc = my_project_collection.find().limit(10)

project_commit_count = {}

for x in mydoc:
    tmp_cnt = my_commit_collection.count_documents({'project_name_info.project_id': x['_id']})
    project_commit_count[x['name']] = tmp_cnt

print(len(project_commit_count))
print(project_commit_count)



