import argparse
from meet_elasticsearch.test import test


def _build_table(name, results):
    """Generate a pretty CSV string from a result set.

    :param name: The name of the table.
    :param results: The result set.
    :return: 
    """
    measurements = sorted([measurement for measurement in
                    next(iter(results.values())).keys()])

    table = ','.join([key.replace('_', ' ') for key in [name] + measurements])\
            + '\n'

    for typo in iter(results):
        values = [str(results[typo][m]) for m in measurements]
        table += ','.join([typo.replace('_', ' ')] + values) + '\n'

    return table


def test_and_print(strategy_a, strategy_b):
    results = test(strategy_a, strategy_b)
    tables = [_build_table(name, result) for name, result in results]
    print('\n\n'.join(tables))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Execute the tests for two search strategies')
    parser.add_argument('strategy_a', metavar='A', type=str,
                        help='The base strategy to compare')
    parser.add_argument('strategy_b', metavar='B', type=str,
                        help='The alternative strategy to compare')

    args = parser.parse_args()

    test_and_print(args.strategy_a, args.strategy_b)
