import argparse
from meet_elasticsearch.test import test


def _build_table(name, results):
    """Generate a pretty CSV string from a result set.

    :param name: The name of the table.
    :param results: The result set.
    :return: 
    """

    measurements = sorted([measurement for measurement in results[0][1].keys()])

    table = ','.join([key.replace('_', ' ') for key in [name] + measurements])\
            + '\n'

    for typo, result in results:
        values = [str(result[m]) for m in measurements]
        table += ','.join([typo.replace('_', ' ')] + values) + '\n'

    return table


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Execute the tests for two search strategies')
    parser.add_argument('strategy_a', metavar='A', type=str,
                        help='The base strategy to compare')
    parser.add_argument('strategy_b', metavar='B', type=str,
                        help='The alternative strategy to compare')

    args = parser.parse_args()

    print('\n\n'.join([_build_table(name, result) for name, result
                       in test(args.strategy_a, args.strategy_b)]))
