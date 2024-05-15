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

def search_genres(ganer):
    sql_date = "SELECT title, `genres`, year, `imdb.rating` FROM movies WHERE `genres`\
                LIKE '%" + ganer + "%' ORDER BY `imdb.rating` DESC LIMIT 10"
    dbconnect = Test_progect.DbSql()
    result = dbconnect.other_select(sql_date)
    return result


def print_result(res):
    heads = ['Название: ', 'Жанр: ', 'Год выпуска: ', 'Рейтинг: ']
    print(heads[0].center(50), heads[1].center(50), heads[2].center(20), heads[3].center(20))
    for row in res:
        ganer = str(row[1]).replace('}','').replace('{','')
        print(row[0].ljust(50), ganer.center(50), str(row[2]).center(20), str(row[3]).center(20))

