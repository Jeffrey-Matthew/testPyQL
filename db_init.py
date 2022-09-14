#!/usr/bin/env python3

import os
import sqlite3


def db_init_users():

    users = [
        ('admin', 'SuperSecret'),
        ('elliot', '123123123'),
        ('tim', '12345678')
    ]

    conn = sqlite3.connect('db_users.sqlite')
    c = conn.cursor()
    c.execute("CREATE TABLE users (username text, password text, failures int, mfa_enabled int, mfa_secret text)")

    for u,p in users:
        c.execute("INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES ('%s', '%s', '%d', '%d', '%s')" %(u, p, 0, 0, ''))

    conn.commit()
    conn.close()





if __name__ == '__main__':
    db_init_users()

