import sqlite3

db_name = '''test.db'''

print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:\n ")
try:
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute("select store.title from store")
        stores = cursor.fetchall()
        for i in range(len(stores)):
            print(f"{i + 1}. {stores[i][0]}")
except sqlite3.Error as e:
    print(e)
print(" ")

while True:
    number = int(input("Введите число: "))
    print(" ")
    if number == 0:
        break
    else:
        try:
            with sqlite3.connect(db_name) as connection:
                cursor = connection.cursor()
                sql = f'''
                select p.title, c.title, p.unit_price, p.stock_quantity from products as p
                inner join categories as c on p.category_code = c.code
                where store_id = {number}
                '''
                cursor.execute(sql)
                products = cursor.fetchall()
        except sqlite3.Error as e:
            print(e)
        if len(products) == 0:
            print("Такого магазина нет\n ")
        else:
            for product in products:
                print(f"Название продукта: {product[0]}\nКатегория: {product[1]}\nЦена: {product[2]}\nКоличество на складе: {product[3]}\n ")
