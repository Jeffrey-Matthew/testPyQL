#!/usr/bin/env python3

import os
import sqlite3

def db_init_posts():

    conn = sqlite3.connect('db_posts.sqlite')
    c = conn.cursor()
    c.execute("CREATE TABLE posts (date date, username text, text text)")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    db_init_users()

