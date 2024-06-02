import sys
import mysql.connector


class DbSql:
    db_conf = {'host':
               '192.168.1.3',
               'user': 'root',
               'port': '6033',
               'password': 'passw',
               'database': 'movies'}

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(**DbSql.db_conf)
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Connection Error:{e}")
            sys.exit(1)

    def select_table(self, table):
        table_rows = f"SELECT * FROM {table}"
        self.cursor.execute(table_rows)
        rows = self.cursor.fetchall()
        return rows

    def other_select(self, request):
        try:
            self.cursor.execute(request)
        except mysql.connector.Error as e:
            print(f"Connection Error:{e}")
            return 1
        rows = self.cursor.fetchall()
        return rows

    def insert(self, arg):
        sql_date_ins = 'INSERT INTO keyword_tab (`keywords`) VALUES (%s)'
        ins_key_word = [arg]
        try:
            self.cursor.execute(sql_date_ins, ins_key_word)
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Connection Error:{e}")
            return 1

    def __del__(self):
        self.connection.close()
