import sys
import mysql.connector


class DbSql:
    db_conf = {'host':
               '172.17.0.1',
               'user': 'root',
               'port': '6033',
               'password': 'passw',
               'database': 'movies'}
    db_tables = {"users": ["id", "name", "age"],
                 "product": ["pid", "prod", "quantity"],
                 "sales": ["sid", "pid", "id"]}

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
        self.cursor.execute(request)
        rows = self.cursor.fetchall()
        return rows

    def __del__(self):
        self.connection.close()


dbconnect = DbSql()
sql_data_show = "SELECT title, year, `imdb.rating` FROM movies WHERE plot LIKE '%friend%' \
                 ORDER BY `imdb.rating` DESC LIMIT 10"
sql_data_show2 = "SELECT count(*) FROM movies"
sql_data_show3 = "SELECT DISTINCT `genres`FROM movies"
sql_data_show4 = "SELECT * FROM movies"
result = dbconnect.other_select(sql_data_show4)

#for row in result:
#     print(row)
