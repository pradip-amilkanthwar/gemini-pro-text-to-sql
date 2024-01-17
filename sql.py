import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

table_info = """
create table student_info(name varchar(100),class varchar(50),section varchar(50),marks int);
"""

cursor.execute(table_info)

cursor.execute("""insert into student_info values('Pradip','Data Analyst','A',78)""")
cursor.execute(
    """insert into student_info values('Lakshmikant','Data Analyst','A',86)"""
)
cursor.execute(
    """insert into student_info values('Chandrakant','Data Science','A',94)"""
)
cursor.execute("""insert into student_info values('Latika','Data Science','A',82)""")
cursor.execute("""insert into student_info values('Deepika','Data Analyst','A',79)""")


print("Records inserted successfully ... ")

data = cursor.execute("SELECT * FROM student_info")

for row in data:
    print(row)

connection.commit()
connection.close()
