import sqlite3
from pathlib import Path
from datetime import datetime
# class definition



class Dog:
    def __init__(self):
        self.name = "dog"


class Person:
    # class attribute
    arm = 2
    eye = 2
    database_address = Path('s03/db.sqlite3')

    # initializer method
    # init object attribute
    def __init__(self, username, password):
        # object attribute
        self.create_table()
        self.username = username
        self.password = password
        # self.create_at = datetime.now()
        self.id = None
        self.my_dog = Dog()

    # custom method
    # we call def in class as method
    def say_hello(self):
        return f"hello I'm {self.name}"

    def __str__(self):
        return f"Person(name='{self.username}')"

    def __repr__(self):
        return f"Person(name='{self.username}')"

    def save(self):
        conn = sqlite3.connect(self.database_address)
        cursor = conn.cursor()
        cursor.execute("insert into person (username,password) values (?,?);",
                       (self.username, self.password))
        conn.commit()
        conn.close()

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect(cls.database_address)
        cursor = conn.cursor()
        cursor.execute(
            "create table if not exists person(id integer primary key , username text unique,password text);")
        conn.commit()
        conn.close()

    @classmethod
    def filter(cls, **kwargs):
        # list comprehentions
        where_clause = [f"{key}='{value}'" for key, value in kwargs.items()]
        where = " and ".join(where_clause)
        # print(where)
        conn = sqlite3.connect(cls.database_address)
        cursor = conn.cursor()
        cursor.execute(
            f"select id,username,password from person where {where};")
        results = cursor.fetchall()
        output = []
        for result in results:
            p = cls(result[1], result[2])
            p.id = result[0]
            output.append(p)

        conn.commit()
        conn.close()
        return output


# how to make objects from class
# p1 = Person("mohammad1", "123")
# p1.save()


# p2 = Person.filter(username="mohammad", password="123")
# print(p2[0])
p2 = Person.filter(password="123")
print(p2)


# p2 = Person("ali")
# print(p1.arm)
# print(p2.arm)
# print(p1.name)
# print(p1.say_hello())
# print(p2.say_hello())
# pl.save()
# print(p1)

# ORM
# object relation map
# Object-Relational Mapping (ORM) is a technique that lets
# you query and manipulate data from a database using an
# object-oriented paradigm. When talking about ORM,
# most people are referring to a library that implements
# the Object-Relational Mapping technique, hence the phrase
# "an ORM".
# An ORM library is a completely ordinary library written
# in your language of choice that encapsulates the code
# needed to manipulate the data, so you don't use SQL
# anymore; you interact directly with an object in the
# same language you're using


# relational database management system (rdbms)
# The software used to store, manage, query,
# and retrieve data stored in a relational
# database is called a relational database
# management system (RDBMS). The RDBMS provides
# an interface between users and applications
# and the database, as well as administrative
# functions for managing data storage, access,
# and performance
