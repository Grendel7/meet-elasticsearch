from functools import reduce
from random import choice
from statistics import mean, stdev

from . import database, elasticsearch, query, typo
from .calculations import precision, recall, reciprocal_rank


def _test_internal(typo_function, strategies):
    """Test the search results using a given search strategy.

    :param typo_function: The name of the function in the typo module to use.
    :return: A formatted table string.
    """
    all_companies = list(database.all_companies())

    results = {}

    for strategy_name in strategies:
        strategy = getattr(query, strategy_name+'_query')

        precisions = []
        recalls = []
        reciprocal_ranks = []

        models = [choice(all_companies) for i in range(0, 999)]
        terms = [typo_function(model['name']) for model in models]

        requests = []

        for term in terms:
            requests.append({})
            requests.append({
                "query": {
                    "multi_match": strategy(term)
                }
            })

        responses = elasticsearch.msearch(requests, 'company', 'company')

        for i, result in enumerate(responses['responses']):
            received = 0
            position = None

            for pos, hit in enumerate(result['hits']['hits']):
                if int(hit['_id']) == models[i]['id']:
                    position = pos

                received += 1

            precisions.append(precision(position, received))
            recalls.append(recall(position))
            reciprocal_ranks.append(reciprocal_rank(position))

        results[strategy_name] = {
            'precision_mean': mean(precisions),
            'precision_stdev': stdev(precisions),
            'recall_mean': mean(recalls),
            'recall_stdev': stdev(recalls),
            'reciprocal_mean': mean(reciprocal_ranks),
            'reciprocal_stdev': stdev(reciprocal_ranks),
        }

    return results


def test(strategy_a, strategy_b):
    functions = [typo.raw, typo.random_word, typo.random_word_part,
                 typo.add_space, typo.add_space_word, typo.remove_space,
                 typo.levenshtein_1, typo.levenshtein_2,
                 typo.levenshtein_word_1, typo.levenshtein_word_2]

    return [(function.__name__, _test_internal(function, [strategy_a, strategy_b]))
            for function in functions]