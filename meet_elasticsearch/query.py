def base_query(term):
    return {
        'query': term,
        'fields': ['name']
    }


def fuzzy_query(term):
    return {
        'query': term,
        'fields': ['name'],
        'fuzziness': 'AUTO'
    }


def trigram_single_match_query(term):
    return {
        'query': term,
        'fields': ['name.trigram'],
    }


def trigram_multi_match_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.trigram'],
    }


def bigram_single_match_query(term):
    return {
        'query': term,
        'fields': ['name.bigram'],
    }


def bigram_multi_match_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
    }


def bigram_multi_match_most_fields_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
        'type': 'most_fields'
    }


def bigram_multi_match_cross_fields_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
        'type': 'cross_fields'
    }


def bigram_multi_match_and_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
        'operator': 'and'
    }


def bigram_multi_match_most_fields_and_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
        'type': 'most_fields',
        'operator': 'and'
    }


def bigram_multi_match_most_fields_and_fuzzy_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
        'type': 'most_fields',
        'operator': 'and',
        'fuzziness': 'AUTO'
    }


def bigram_multi_match_cross_fields_and_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
        'type': 'cross_fields',
        'operator': 'and'
    }


def bigram_multi_match_phrase_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
        'type': 'phrase',
    }


def bigram_multi_match_phrase_prefix_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram'],
        'type': 'phrase_prefix',
    }


def bigram_trigram_multi_match_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram', 'name.trigram'],
    }


def bigram_multi_match_boosted_name_query(term):
    return {
        'query': term,
        'fields': ['name^5', 'name.bigram'],
        'type': 'most_fields',
    }


def bigram_multi_match_boosted_bigram_query(term):
    return {
        'query': term,
        'fields': ['name', 'name.bigram^5'],
        'type': 'most_fields',
    }
