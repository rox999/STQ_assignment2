import datetime
import pymongo
import networkx as nx
import pytest

def create_network():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["smartshark"]
    my_project_collection = mydb["project"]
    my_commit_collection = mydb["commit_with_project_info"]
    my_file_action_collection = mydb["file_action"]

    start = datetime.datetime(2017, 2, 20)
    end = datetime.datetime(2017, 2, 23)

    mydoc = my_commit_collection.find({'$and': [{'project_name_info.name': 'kafka'}, {'committer_date': {'$gte': start, '$lt': end}}]})

    kafka_commit_list = []

    for x in mydoc:
        kafka_commit_list.append(x['_id'])
    print(len(kafka_commit_list))
    print(kafka_commit_list)

    actions = {}

    for commit_id in kafka_commit_list:
        if commit_id not in actions:
            actions[commit_id] = []
        actions_with_commit_id = my_file_action_collection.find({'commit_id': commit_id})
        for item in actions_with_commit_id:
            actions[commit_id].append(item['file_id'])

    print(len(actions))
    print(actions)


    graph = nx.Graph()

    for commit_id in actions:
        for file_id in actions[commit_id]:
            graph.add_node(file_id)

    for commit_id in actions:
        files_to_deal_with = actions[commit_id]
        for i in range(1, len(files_to_deal_with)):
            for j in range(0,i):
                graph.add_edge(files_to_deal_with[i], files_to_deal_with[j])

    print(len(graph.nodes))
    print(graph.nodes)
    print(len(graph.edges))

    counter = 0;
    for edge in graph.edges:
        print(edge)
        counter += 1
        if counter == 5:
            break
    return graph

