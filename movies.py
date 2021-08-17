import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()


cursor.execute('SELECT * FROM MOVIES')
obj = cursor.fetchall()

row_count = len(obj)
# print(row_count)
print('Name               ', 'Actor              ', 'Actress            ', 'Year of release    ', 'Director           ')
print("---------------------------------------------------------------------------------------------------------------")

i = 0

while i < row_count:
    print(obj[i][0], ' ' * (18 - len(obj[i][0])), obj[i][1], ' ' * (18 - len(obj[i][1])), obj[i][2], ' ' * (18 - len(obj[i][2])),
          obj[i][3], ' ' * (14), obj[i][4], ' ' * (18 - len(obj[i][4])), )
    i = i + 1
connection.commit()
connection.close()
