import Test_progect


def get_list_genres ():
    dbconnect = Test_progect.DbSql()
    sql_data_show3 = "SELECT DISTINCT `genres` FROM movies"
    result = dbconnect.other_select(sql_data_show3)
    genres = []
    for row in result:
        genres_old = []
        for word in row:
            genres_old = genres_old + list(word)
        for word2 in genres_old:
            genres.append(word2)

    genres = list(set(genres))
    print(f"Всего жанров - {len(genres)}")
    i = 0
    j = 3
    while i < len(genres):
        if i <= j:
            print(genres[i].ljust(12),end='')
            i += 1
        else:
            print("")
            j += 4


def search_genres(ganer,*year):
    if len(year) == 0:
        sql_date = (f"SELECT id, title, `genres`, year, `imdb.rating` FROM movies WHERE `genres`\
                LIKE '%{ganer}%' ORDER BY `imdb.rating` DESC LIMIT 10")
    elif len(year) == 1:
        sql_date = (f"SELECT id, title, `genres`, year, `imdb.rating` FROM movies WHERE `genres`\
                        LIKE '%{ganer}%' AND `year`={year[0]} ORDER BY `imdb.rating` DESC LIMIT 10")
    else:
        sql_date = (f"SELECT id, title, `genres`, year, `imdb.rating` FROM movies WHERE `genres`\
                LIKE '%{ganer}%' AND `year` IN {year} ORDER BY `imdb.rating` DESC LIMIT 10")
    dbconnect = Test_progect.DbSql()
    result = dbconnect.other_select(sql_date)
    return result


def search_id(id):
    sql_date = (f"SELECT `title`, `plot` FROM movies WHERE id={id}")
    dbconnect = Test_progect.DbSql()
    result = dbconnect.other_select(sql_date)
    for row in result:
        print(row[0])
        print(row[1])
#    print(str(result[0]).strip("()"),"\t", str(result[1]).strip("()"))


def print_result(res):
    heads = ['Название: ', 'Жанр: ', 'Год выпуска: ', 'Рейтинг: ']
    print(heads[0].center(58), heads[1].center(53), heads[2].center(20), heads[3].center(20))
    i = 1
    spisok = {}
    for row in res:
        print(str(i).rjust(2), row[1].ljust(55), (str(row[2]).strip("{}")).center(51), str(row[3]).center(20), str(row[4]).center(20))
        spisok[i] = row[0]
        i += 1
#    print(spisok)
    return spisok
