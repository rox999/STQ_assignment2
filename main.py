

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["smartshark"]
mycol1 = mydb["project"]
mycol2 = mydb["commit_with_project_info"]
mycol3 = mydb["comments_with_issue_and_project_info"]
mycol4 = mydb["people"]
mycol5 = mydb["issue_comment"]
mydoc = mycol1.find().limit(20)
mydoc2 = mycol3.find({'issue_info.project_name_info.name': 'zookeeper'}).limit(20)

all_projects = []
commit_count = {}
kafka_developers = []
kafka_developers_names = []

for x in mydoc2:
    kafka_developers.append(x['author_id'])
print(len(kafka_developers))

kafka_developers = list(set(kafka_developers))
print(len(kafka_developers))

for x in kafka_developers:
    mydoc3 = mycol4.find({'_id': x}).limit(10)
    for y in mydoc3:
        kafka_developers_names.append(y['name'])

#print(kafka_developers_names)

issue_count_for_developers = {}

for developer in kafka_developers:
    mydoc4 = mycol5.find({'author_id': developer}).limit(10)
    issues = []
    for y in mydoc4:
        issues.append(y['issue_id'])
    issues = list(set(issues))
    issue_count_for_developers[developer] = len(issues)

print(issue_count_for_developers)

#print(kafka_developers)

for x in mydoc:
  all_projects.append(x['name'])

print(all_projects)

for project in all_projects:
    # tmp_cnt =
    tmp_cnt = mycol2.count_documents({'project_name_info.name': project})
    commit_count[project] = tmp_cnt

print(commit_count)



