from math import log


def precision(position, received):
    """Calculate the precision given a correct result position and the total number of received documents.

    The precision of a search result is:
    # of relevant results / # of results

    :param position: The position of the correct result or None.
    :param received: The number of hits.
    :return:
    """
    if received > 0:
        return (0 if position is None else 1) / float(received)
    else:
        return 0


def recall(position):
    """Calculate the recall given a result position.

    The recall of a search result is:
    # of received relevant results / # of total relevant results

    :param position: The position of the correct result or None.
    :return:
    """
    return (0 if position is None else 1) / 1.0


def reciprocal_rank(position):
    """Calculate the reciprocal rank of a result position.

    The reciprocal rank is 1 / position of the search result.

    :param position:
    :return:
    """
    if position is None:
        return 0
    else:
        return 1 / (position + 1.0)


def f_score(position, received):
    """Calculate the F1-score of the result.

    The F1-score is the harmonic mean of the precision and the average.

    :param position:
    :param received:
    :return:
    """
    p = precision(position, received)
    r = recall(position)

    if r == 0 or p == 0:
        return 0
    else:
        return 2 * (p * r) / (p + r)


def ndcg(position):
    """Calculate the normalized Distributive Cumulative Gain of the result.

    Given how there is only one relevant result, this is a heavily simplified
    version of nDCG. Normally, the DCG of a specific result set is:

    relevance / log2(position + 1) for all results in the result set

    In this case, the relevance score of 1 is used for the correct document and
    0 for all other documents. Because of that, we don't need to calculate
    scores for all results, only for the correct one (because everything else
    is 0 anyways.

    The nDCG is the DCG / ideal DCG (i.e. the documents would be perfectly
    sorted on relevance). However, with one document on the first result, it
    would be:

    1 / log2(1 + 1) = 1

    Making the final calculation:

    DCG / 1

    That is why this implementation is heavily simplified.

    :param position:
    :return:
    """
    if position is None:
        return 0
    else:
        return 1 / log(position + 2, 2)