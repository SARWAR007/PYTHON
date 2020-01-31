import sqlite3
connection = sqlite3.connect('sqllite3_tutorial.db')
cursor = connection.cursor()

#cursor.execute('CREATE TABLE STUDENT (NAME VARCHAR(20),COLLEGE VARCHAR(20))')

cursor.execute('INSERT INTO STUDENT VALUES(?,?)',('FARHAN','NIST'))

connection.commit()
