import sqlite3

db_name = 'hw_8.db'

print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0")
print(" ")
with sqlite3.connect(db_name) as connection:
    try:
        cursor = connection.cursor()
        cursor.execute("select title from cities")
        cities = cursor.fetchall()
        for i in range(len(cities)):
            print(f"{i + 1}. {cities[i][0]}")
    except sqlite3.Error as e:
        print(e)
print(" ")

while True:
        number = int(input("Введите номер города: "))
        if number == 0:
            break
        else:
            with sqlite3.connect(db_name) as connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute(f'select st.first_name, st.last_name, co.title, ci.title, ci.area from students as st inner join cities as ci on st.city_id = ci.id inner join countries as co on ci.country_id = co.id where ci.id is {number}')
                    students = cursor.fetchall()
                except sqlite3.Error as e:
                    print(e)
            # Вот способ покрасивее:
            # print(" ")
            # print(f"Country: {students[0][2]}, city: {students[0][3]}, area of city: {students[0][4]}")
            # for student in students:
            #     print(student[0], student[1])
            # print(" ")
            # Способ из условий задачи:
            print(" ")
            if len(students) == 0:
                print("    Такого города нет, или нет студентов, живущих в этом городе")
            else:
                for student in students:
                    print(f"    First name: {student[0]}, last name: {student[1]}, country: {student[2]}, city: {student[3]}, area of city: {student[4]}")
            print(" ")
