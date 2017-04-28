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
