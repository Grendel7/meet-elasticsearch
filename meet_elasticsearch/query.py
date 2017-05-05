def base(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name']
            }
        }
    }


def fuzzy(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name'],
                'fuzziness': 'AUTO'
            }
        }
    }


def trigram_single_match(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name.trigram']
            }
        }
    }


def trigram_multi_match(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.trigram']
            }
        }
    }


def bigram_single_match(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name.bigram']
            }
        }
    }


def bigram_multi_match(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram']
            }
        }
    }


def bigram_most_fields(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram'],
                'type': 'most_fields'
            }
        }
    }


def bigram_cross_fields(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram'],
                'type': 'cross_fields'
            }
        }
    }


def bigram_and(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram'],
                'operator': 'and'
            }
        }
    }


def bigram_most_fields_and(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram'],
                'type': 'most_fields',
                'operator': 'and'
            }
        }
    }


def bigram_most_fields_and_fuzzy(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram'],
                'type': 'most_fields',
                'operator': 'and',
                'fuzziness': 'AUTO'
            }
        }
    }


def bigram_cross_fields_and(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram'],
                'type': 'cross_fields',
                'operator': 'and'
            }
        }
    }


def bigram_phrase(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram'],
                'type': 'phrase'
            }
        }
    }


def bigram_phrase_prefix(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram'],
                'type': 'phrase_prefix'
            }
        }
    }


def bigram_trigram(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram', 'name.trigram']
            }
        }
    }


def bigram_boosted_name(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name^5', 'name.bigram'],
                'type': 'most_fields'
            }
        }
    }


def bigram_boosted_bigram(term):
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.bigram^5'],
                'type': 'most_fields'
            }
        }
    }
