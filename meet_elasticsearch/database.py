from faker import Factory
import sqlite3

fake = Factory.create('nl_NL')

_connection = sqlite3.connect('database.sqlite')
_connection.row_factory = sqlite3.Row
_cursor = _connection.cursor()


def delete_table():
    _cursor.execute('DROP TABLE IF EXISTS companies')
    _connection.commit()


def create_table():
    _cursor.execute('CREATE TABLE companies ('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                    'name TEXT NOT NULL, '
                    'street TEXT NOT NULL, '
                    'postal_code TEXT NOT NULL, '
                    'city TEXT NOT NULL, '
                    'phone_number TEXT NOT NULL, '
                    'email TEXT NOT NULL)')
    _connection.commit()


def populate(count):
    for i in range(0, count):
        _cursor.execute('INSERT INTO companies (name, street, postal_code, '
                        'city, phone_number, email) '
                        'VALUES (?, ?, ?, ?, ?, ?)', [
                            fake.company(), fake.street_address(),
                            fake.postcode(),
                            fake.city(), fake.phone_number(),
                            fake.company_email()
                        ])

    _connection.commit()


def all_companies():
    return _cursor.execute('SELECT * FROM companies')
