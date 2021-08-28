import sqlite3, json


def get_first(x):
    return x[0]


class DataBase:
    def __init__(self, way='../data/data'):
        # try:
        conn = sqlite3.connect(way, check_same_thread=False)
        # except
        self.connection = conn

    def get_connection(self):
        return self.connection

    def __del__(self):
        self.connection.close()


class Users:
    def __init__(self, conn):
        self.connection = conn

    def insert(self, username, identification):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users (id, name) VALUES (?,?)''', (username, identification,), )
        self.connection.commit()
        return "OK"

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id),), )
        user_info = cursor.fetchone()
        bar = tuple(map(get_first, cursor.description))
        user = dict()

        for parameter in range(len(bar)):
            user[bar[parameter]] = user_info[parameter]
        return user

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM users")
        ids = tuple(map(get_first, cursor.fetchall()))
        return ids

    def update_user(self, identification, new_info):
        if len(new_info) < 20:
            cursor = self.connection.cursor()
            for parameter in new_info:
                cursor.execute("UPDATE users set {} = ? where id = ?".format(parameter),
                               (new_info[parameter], identification,), )
        self.connection.commit()
        return "OK"
