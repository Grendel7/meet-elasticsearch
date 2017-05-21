def base(term):
    """
    Completely standard Elasticsearch behaviour without any customization.
    """
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name']
            }
        }
    }


def fuzzy(term):
    """
    Search the regular name field with Fuzzy matching
    """
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
    """
    Search only the Trigram field (n-gram with length 3)
    """
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name.trigram']
            }
        }
    }


def trigram_multi_match(term):
    """
    Search the Trigram field and regular name field and combine them with the default "best fields" method.
    """
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.trigram']
            }
        }
    }


def trigram_most_fields(term):
    """
    Search the trigram field and regular name field and combine them with the "most fields" method.
    """
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.trigram'],
                'type': 'most_fields'
            }
        }
    }


def trigram_cross_fields(term):
    """
    Search the trigram field and regular name field and combine them with the "cross fields" method.
    """
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.trigram'],
                'type': 'cross_fields'
            }
        }
    }


def trigram_phrase(term):
    """
    Search the trigram field and regular name field and combine then with the "phrase" method
    """
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.trigram'],
                'type': 'phrase'
            }
        }
    }


def trigram_boosted_name(term):
    """
    Search the trigram field and regular name field and boost the name field.
    """
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name^5', 'name.trigram'],
                'type': 'most_fields'
            }
        }
    }


def trigram_boosted_trigram(term):
    """
    Search the trigram field and regular name field and boost the trigram field.
    """
    return {
        "query": {
            "multi_match": {
                'query': term,
                'fields': ['name', 'name.trigram^5'],
                'type': 'most_fields'
            }
        }
    }
