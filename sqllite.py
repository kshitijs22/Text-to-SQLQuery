# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('employee1.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 
  
# Creating table 
table ="""CREATE TABLE EMPLOYEE(NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255));"""
cursor.execute(table)
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Kshitij', 'Data Science', 'A')''') 
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Divyam', 'Data Science', 'B')''') 
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Sookha', 'Devops', 'C')''') 
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Rajput', 'IIT', 'C')''') 
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Hashir', 'SDE', 'C')''')
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Shashwat', 'SDE', 'C')''')
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Shiva', 'Quantum', 'D')''')
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM EMPLOYEE''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()