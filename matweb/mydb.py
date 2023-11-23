import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Josh12$'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE matrimony')

print('All done!!!!!!!!')