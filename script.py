import sqlite3
conn = sqlite3.connect("instance/campus_connect.db")
cursor = conn.cursor()
cursor.execute("UPDATE student SET course_id = ? WHERE course_id IS NULL",(1,))
cursor.execute("UPDATE student SET course = ? WHERE course IS NULL",('Python',))

conn.commit()
conn.close()
print("Done: Old students updated with course_id = 1")