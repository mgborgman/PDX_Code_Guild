__author__ = 'Matt Borgman'

from peewee import *
import errno


# create SQLite database named users.db and assign it to db
db = SqliteDatabase('users.db')

class Customer(Model):
    ''' name, email, and password that make up the Customer which
        will go into the database
    '''
    name = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db


def create_table():
    ''' connect to database db and create table from Customer class '''
    try:
        db.connect()
        db.create_table(Customer)
        print("OK")
    except DatabaseError as err:
        print("Table already exists")


# TESTING
# create_table()
#
# print("wait...")
#
# create_table()

