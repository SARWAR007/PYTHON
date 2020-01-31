import sqlite3

con = sqlite3.connect("Card.db")
print("Database opened successfully")

con.execute("create table CreditCard (transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, Spends TEXT NOT NULL, Month DATE NOT NULL, Amount Number NOT NULL)")

print("Table created successfully")

con.close()
