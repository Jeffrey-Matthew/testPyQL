#!/usr/bin/env python3

import os
import sqlite3
def db_init_users():
    users = [
        ('admin', 'SuperSecret'),
        ('elliot', '123123123'),
        ('tim', '12345678')
    ]
    conn_i = sqlite3.connect('db_users.sqlite')
    c_val = conn_i.cursor()
    c_val.execute("CREATE TABLE users (username text, password text, failures int, mfa_enabled int, mfa_secret text)")
    conn_i.commit()
    conn_i.close()

def db_init_posts():
    conn = sqlite3.connect('db_posts.sqlite')
    c = conn.cursor()
    c.execute("CREATE TABLE posts (date date, username text, text text)")
    conn.commit()
    conn.close()

if __name__ == '__main__':  
    db_init_users()
    db_init_posts()
