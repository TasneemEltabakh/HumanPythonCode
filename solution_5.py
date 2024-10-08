import sqlite3
from sqlite3 import Error
def sql_connection():
   try:
     conn = sqlite3.connect('mydatabase.db')
     return conn
   except Error:
     print(Error)
def sql_table(conn):
   cursorObj = conn.cursor()
   cursorObj.execute("CREATE TABLE agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")
   print("\nagent_master file has created.")
   
   # adding a new column in the agent_master table
   cursorObj.execute("""
   ALTER TABLE agent_master
   ADD COLUMN FLAG BOOLEAN;
   """)
   print("\nagent_master file altered.")
   conn.commit()
   
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")
