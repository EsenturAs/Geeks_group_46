import sqlite3

db_name = '''hw.db'''


def create_table(sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


sql_to_create_product_table = '''
create table products (
    id integer primary key autoincrement,
    product_title varchar(200) not null,
    price float(10, 2) not null default 0.0,
    quantity integer not null default 0
)
'''


def add_product(product):
    try:
        sql = '''insert into products 
        (product_title, price, quantity)
        VALUES (?, ?, ?)
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as e:
        print(e)


def change_quantity(product):
    try:
        sql = '''update products set quantity = ? 
        where id = ?
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as e:
        print(e)


def change_price(product):
    try:
        sql = '''update products set price = ? 
        where id = ?
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as e:
        print(e)


def delete_product(id):
    try:
        sql = '''delete from products where id = ?'''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)


def print_all_products():
    try:
        sql = '''
        select * from products
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def print_all_products_by_price_and_quantity(limits):
    try:
        sql = '''
        select * from products
        where price < ? and quantity > ?
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, limits)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def search_product(key_word):
    try:
        sql = "select * from products where product_title like '%" + key_word + "%'"
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def add_15_products():
    add_product(('Milk', 93.45, 5))
    add_product(('Chicken', 100.5, 14))
    add_product(('Water', 20.2, 20))
    add_product(('Pie', 140.49, 4))
    add_product(('Tea', 50.43, 9))
    add_product(('Chocolate', 83.69, 3))
    add_product(('Candy', 30.5, 8))
    add_product(('Watermelon', 10.40, 90))
    add_product(('Tomato', 30.34, 9))
    add_product(('Pickle', 25.25, 25))
    add_product(('Meat', 39.58, 2))
    add_product(('Fish', 28.59, 18))
    add_product(('Apple', 82.39, 20))
    add_product(('Orange', 10.56, 4))
    add_product(('Banana', 100.36, 8))


create_table(sql_to_create_product_table)
add_15_products()
change_quantity((20, 2))
change_price((23.0, 3))
delete_product(15)
print_all_products()
print_all_products_by_price_and_quantity((100, 5))
search_product('Water')
