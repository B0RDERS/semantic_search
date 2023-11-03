import json
from embeddings import get_embeddings, get_embedding
from pymongo.mongo_client import MongoClient

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

#connect to mongodb atlas
atlas_url = f"mongodb+srv://{config['MONGODB_UNAME']}:{config['MONGODB_PWORD']}@restapi.z9hbcdu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(atlas_url)
search_min_score = 0

# populate mongodb
def add_items(items):
    embeddings = get_embeddings([i['name'] for i in items])
    for idx, item in enumerate(items):
        item['embedding']=embeddings[idx]
    coll=client['groceryApp']['items']
    coll.insert_many(items)

# query mongodb
def find_items(item):
    coll=client['groceryApp']['items']
    results = coll.aggregate([
        {"$vectorSearch": {
            "queryVector": get_embedding(item),
            "path": "embedding",
            "numCandidates": 100,
            "limit": 10,
            "index": "vectorIndex",
        }},
        {"$project": {
            "_id": 0, # Exclude the "_id" field
            "embedding": 0,  # Exclude the "embedding" field
            "score": { "$meta": "vectorSearchScore" } # Include search score in result
        }}
        ])
    return [{k:v for k, v in i.items() if k != ''} for i in results if i['score'] > search_min_score]

# clear db table
def clear():
    client['groceryApp']['items'].delete_many({})

def reset():
    clear()
    with open('items.json', 'r') as items_file:
        items = json.load(items_file)
    add_items(items)