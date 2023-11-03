import openai
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    
# connect to openai
openai.organization = config['OPENAI_ORG']
openai.api_key = config['OPENAI_KEY']

# get embeddings
def get_embeddings(strings):
    res=openai.Embedding.create(
        model="text-embedding-ada-002",
        input=strings,
        encoding_format="float"
        )
    return [i['embedding'] for i in res['data']]

def get_embedding(string):
    res=openai.Embedding.create(
        model="text-embedding-ada-002",
        input=string,
        encoding_format="float"
        )
    return res['data'][0]['embedding']
