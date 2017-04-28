from elasticsearch.client import IndicesClient
from . import elasticsearch
from . import database


def _convert_to_doc(record):
    return {
        'name': record['name'],
    }


def create():
    return IndicesClient(elasticsearch).create('company', {
        "settings": {
            "index": {
                "number_of_replicas": 0
            },
            "analysis": {
                "analyzer": {
                    "bigram_analyzer": {
                        "type": "custom",
                        "tokenizer": "bigram_tokenizer",
                        "filter": [
                            "standard",
                            "lowercase"
                        ]
                    },
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
                    "bigram_tokenizer": {
                        "type": "ngram",
                        "min_gram": 2,
                        "max_gram": 2,
                        "token_cars": ['letter', 'digit']
                    },
                    "trigram_tokenizer": {
                        "type": "ngram",
                        "min_gram": 3,
                        "max_gram": 3,
                        "token_cars": ['letter', 'digit']
                    }
                },
            }

        },
        "mappings": {
            "company": {
                "properties": {
                    "name": {
                        "type": "text",
                        "fields": {
                            "bigram": {
                                "type": "text",
                                "analyzer": "bigram_analyzer",
                            },
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
    return IndicesClient(elasticsearch).delete('company')


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
        actions.append(_convert_to_doc(record))

    elasticsearch.bulk(actions)
