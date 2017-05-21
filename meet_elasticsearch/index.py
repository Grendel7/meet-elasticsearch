from elasticsearch.client import IndicesClient
from . import elasticsearch
from . import database


def create():
    return IndicesClient(elasticsearch).create('company', {
        "settings": {
            "index": {
                "number_of_replicas": 0
            },
            "analysis": {
                "analyzer": {
                    "trigram_analyzer": {
                        "type": "custom",
                        "tokenizer": "trigram_tokenizer",
                        "filter": [
                            "standard",
                            "lowercase"
                        ]
                    }
                },
                "tokenizer": {
                    "trigram_tokenizer": {
                        "type": "ngram",
                        "min_gram": 3,
                        "max_gram": 3,
                        "token_chars": ['letter', 'digit']
                    }
                }
            }
        },
        "mappings": {
            "company": {
                "properties": {
                    "name": {
                        "type": "text",
                        "fields": {
                            "trigram": {
                                "type": "text",
                                "analyzer": "trigram_analyzer",
                            }
                        }
                    },
                }
            }
        }
    })


def delete():
    return IndicesClient(elasticsearch).delete('company', ignore=404)


def populate():
    actions = []

    for record in database.all_companies():
        actions.append({
            'index': {
                '_index': 'company',
                '_type': 'company',
                '_id': record['id']
            }
        })
        actions.append({
            'name': record['name'],
        })

    elasticsearch.bulk(actions)
