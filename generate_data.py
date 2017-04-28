from argparse import ArgumentParser

from meet_elasticsearch import database

if __name__ == "__main__":
    parser = ArgumentParser(
        description='Execute the tests for two search strategies')
    parser.add_argument('-c', dest='count', default=1000,
                        help='the number of records to generate (default: 1000')

    args = parser.parse_args()
    database.delete_table()
    database.create_table()
    database.populate(int(args.count))
