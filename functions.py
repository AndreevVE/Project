import MyClassDB
import re

def get_list_genres ():
    dbconnect = MyClassDB.DbSql()
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


def search_genres_years(genre,*year):
    if len(year) == 0:
        plus_year = ""
    elif len(year) == 1:
        plus_year = (f"AND year={year[0]}")
    else:
        plus_year = (f"AND year IN {year}")
    sql_date = (f"SELECT id, title, `genres`, year, `imdb.rating` FROM movies WHERE `genres`\
    LIKE '%{genre}%' {plus_year} ORDER BY `imdb.rating` DESC LIMIT 10")
    dbconnect = MyClassDB.DbSql()
    result = dbconnect.other_select(sql_date)
    if result == 0 or result == 1:
        print("К сожалению по вашему запросу фильмов не нашли.")
        return 1
    return result


def search_id(spisok_id):
    key = input("Хотите посмотреть описания фильма, введите номер из списка: ")
    if re.match("\d+", key):
        id = spisok_id.get(int(key))
        sql_date = (f"SELECT `title`, cast, `plot`, runtime FROM movies WHERE id={id}")
        dbconnect = MyClassDB.DbSql()
        result = dbconnect.other_select(sql_date)
        for row in result:
           print(f"Название: {row[0]}\nАктеры: {row[1].strip('[]')}\nОписание:\n"
                 f"{row[2]}\nПродолжительность: {row[3]} мин")
    else:
        print("Ошибка! Неверный ID")


def search_key_words_title(key_words):
    key_words = str(key_words).replace(" ", " | ")
    sql_date = (f"SELECT id, title, `genres`, year, `imdb.rating` FROM movies WHERE `title`\
             REGEXP  '{key_words}' OR `plot` REGEXP '{key_words}' OR `cast` REGEXP '{key_words}'\
             ORDER BY `imdb.rating` DESC LIMIT 10")
    dbconnect = MyClassDB.DbSql()
    result = dbconnect.other_select(sql_date)
    if result == 0:
        print("К сожалению по вашему запросу фильмов не нашли.")
        return 1
    return result


def insert_db(words):
    dbconnect = MyClassDB.DbSql()
    for word in words:
        dbconnect.insert(word)





def print_result(res):
    heads = ['Название: ', 'Жанр: ', 'Год выпуска: ', 'Рейтинг: ']
    print(heads[0].center(62), heads[1].center(53), heads[2].center(20), heads[3].center(20))
    i = 1
    spisok = {}
    for row in res:
        print(str(i).rjust(2), row[1].ljust(62), (str(row[2]).strip("{}")).center(51),\
              str(row[3]).center(20), str(row[4]).center(20))
        spisok[i] = row[0]
        i += 1
    return spisok
