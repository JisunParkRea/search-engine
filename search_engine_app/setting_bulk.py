from elasticsearch import Elasticsearch
import json


es = Elasticsearch(hosts='192.168.99.100')

with open("dictionary_data.json", encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())

body = ""
for i in json_data:
    body = body + json.dumps({"index": {"_index": "dictionary", "_type": "dictionary_datas"}}) + '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'

es.bulk(body)

es.indices.create(
    index='dictionary',
    body={
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "nori_tokenizer"
                        }
                    }
                }
            }
        },
        "mappings": {
            "dictionary_datas": {
                "properties": {
                    "id": {
                        "type": "long"
                    },
                    "title": {
                        "type": "text",
                        "analyzer": "my_analyzer"
                    },
                    "content": {
                        "type": "text",
                        "analyzer": "my_analyzer"
                    }
                }
            }
        }
    }
)

