import MyClassDB
import re

import functions


def get_list_genres():                                               # функция выбора и печати списка жанров
    dbconnect = MyClassDB.DbSql()
    sql_data_show3 = "SELECT DISTINCT `genres` FROM movies"
    result = dbconnect.other_select(sql_data_show3)
    genres = []
    genres_old = []
    for row in result:
        genres_old = []
        for word in row:
            genres_old = genres_old + list(word)
        for word2 in genres_old:
            genres.append(word2)                                      # разбор списка списков

    genres = list(set(genres))
    print(f"Всего жанров - {len(genres)}")
    i = 0
    j = 3
    while i < len(genres):                                            # печать в 4 столбца
        if i <= j:
            print(genres[i].ljust(12), end='')
            i += 1
        else:
            print("")
            j += 4                                                


def search_genres_years(genre, *year):                                 # функция поиска по жанру и году
    if len(year) == 0:
        plus_year = ""
    else:
        plus_year = f"AND year IN {year}"
    sql_date = (f"SELECT id, title, `genres`, year, `imdb.rating` FROM movies WHERE `genres`\
    LIKE '%{genre}%' {plus_year} ORDER BY `imdb.rating` DESC LIMIT 10")
    dbconnect = MyClassDB.DbSql()
    result = dbconnect.other_select(sql_date)
    if result == 0 or result == 1:
        print("К сожалению, по вашему запросу фильмов не нашлось.")
        return 1
    return result


def search_id(spisok_id):                                            # поиск по id и печать описания
    key = ''
    while key.lower() != "n":
        key = input("Хотите посмотреть описание фильма, введите номер из списка или N: ")
        if re.match("\d+", key) and int(key) <= 10:
            date_id = spisok_id.get(int(key))                        # id из списка передается в sql
            sql_date = f"SELECT `title`, cast, `plot`, runtime FROM movies WHERE id={date_id}"
            dbconnect = MyClassDB.DbSql()
            result = dbconnect.other_select(sql_date)
            for row in result:
                print(f"Название: {row[0]}\nАктеры: {row[1].strip('[]')}\nОписание:\n"
                      f"{row[2]}\nПродолжительность: {row[3]} мин")
        else:
            print("Ошибка! Неверный номер. Для завершения введите N ")
        continue



def search_key_words_title(key_words):                                 # поиск по ключевым словам
    key_words = str(key_words).replace(" ", " | ")                     
    sql_date = (f"SELECT id, title, `genres`, year, `imdb.rating` FROM movies WHERE `title`\
             REGEXP  '{key_words}' OR `plot` REGEXP '{key_words}' OR `cast` REGEXP '{key_words}'\ 
             ORDER BY `imdb.rating` DESC LIMIT 10")                    # поиск ключевого слова в разных полях
    dbconnect = MyClassDB.DbSql()
    result = dbconnect.other_select(sql_date)
    if result == 0:
        print("К сожалению, по вашему запросу фильмов не нашлось.")
        return 1
    return result

def top_words():                                                  # обращение к таблице ключевых слов
    dbconnect = MyClassDB.DbSql()
    sql_data = f"SELECT `keywords` FROM keyword_tab GROUP BY `keywords` ORDER BY count(*) DESC   LIMIT 10"
    result = dbconnect.other_select(sql_data)
    top_word = []
    for word in result:
        top_word = top_word +list(word)
    return top_word


def insert_db(words):
    dbconnect = MyClassDB.DbSql()
    for word in words:
        dbconnect.insert(word)


def print_result(res):                                               # печать результата поиска и формирование списка id
    heads = ['Название: ', 'Жанр: ', 'Год выпуска: ', 'Рейтинг: ']
    print(heads[0].center(62), heads[1].center(53), heads[2].center(20), heads[3].center(20))
    i = 1
    spisok = {}
    for row in res:                                                    # разбор списка результата поиска sql
        print(str(i).rjust(2), row[1].ljust(62), (str(row[2]).strip("{}")).center(51),
              str(row[3]).center(20), str(row[4]).center(20))
        spisok[i] = row[0]
        i += 1
    return spisok                                                      # возврат списка id
