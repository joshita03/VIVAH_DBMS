import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Josh12$'
)

cur = dataBase.cursor()

cur.execute('''
    use matrimony;
''')

cur.execute('''
    INSERT into website_activities (Activity_name,City) values
                ("Rameshwaram Cafe", "Bangalore"),
                ("Wonderla", "Bangalore"),
                ("Sarojini Shopping", "Delhi"),
                ("Kamlanagar hoping", "Delhi"),
                ("Bandra Sea Link", "Mumbai"),
                ("SL world", "Mumbai");
''')


dataBase.commit()
print("All done")
cur.close()