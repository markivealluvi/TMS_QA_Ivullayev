import mysql.connector as mysql


# ШАГ 1. Добавить новую БД - orders_db
# db = mysql.connect(host="localhost",
#                    user="root",
#                    passwd="linkoln546",
#                    database="test_db")
# cursor.execute("CREATE DATABASE orders_db")
db = mysql.connect(host="localhost",
                   user="root",
                   passwd="linkoln546",
                   database="orders_db")
cursor = db.cursor()
# ШАГ 2. Создать таблицу orders.
# cursor.execute("""CREATE TABLE orders (ord_no VARCHAR(255),
#                purch_amt VARCHAR(255),
#                ord_date VARCHAR(255),
#                customer_id VARCHAR(255),
#                salesman_id VARCHAR(255))""")
# ШАГ 3. Внести данные в таблицу.
# query = "INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
# values = [
#     ("70001", "150.5", "2012-10-05", "3005", "5002"),
#     ("70002", "270.65", "2012-09-10", "3001", "5005"),
#     ("70003", "65.26", "2012-10-05", "3002", "5001"),
#     ("70004", "110.5", "2012-08-17", "3009", "5003"),
#     ("70005", "948.5", "2012-09-10", "3005", "5002"),
#     ("70006", "2400.6", "2012-07-27", "3007", "5001"),
#     ("70007", "5760", "2012-09-10", "3002", "5001"),
#     ("70008", "1983.43", "2012-10-10", "3004", "5006"),
#     ("70009", "2480.4", "2012-10-10", "3009", "5003"),
#     ("70010", "250.45", "2012-06-27", "3008", "5002"),
# ]
# cursor.executemany(query, values)
# db.commit()
# 1) Напечатайте номер заказа, дату заказа и количество для каждого заказа,
#    Который продал продавец под номером: 5002
query = "SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id = 5002"
cursor.execute(query)
print(cursor.fetchall())
# 2) Напечатайте уникальные id продавца(salesman_id). Используйте distinct
query = "SELECT DISTINCT salesman_id FROM orders"
cursor.execute(query)
print(cursor.fetchall())
# 3) Напечатайте по порядку данные о дате заказа, id продавца, номер заказа, количество
query = "SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders"
cursor.execute(query)
print(cursor.fetchall())
# 4) Напечатайте заказы между 70001 и 70007(используйте between, and)
query = "SELECT * FROM orders WHERE ord_no BETWEEN 70001 AND 70007"
cursor.execute(query)
print(cursor.fetchall())

db.close()
