import functions

start_text1 = "Привет! Мы поможем вам найти интересный фильм, чтобы провести вечер нескучно!"
start_text2 = "В нашей базе более 5500 фильмов по 23 жанрам. Удачного поиска!"
start_text3 = "@2024"

print("\n", start_text1.center(100), "\n", start_text2.center(100))
print(start_text3.center(100))

while True:
    action = {0: "Exit", 1: "Поиск по жанру и году", 2: "Поиск по году", 3: "Поиск по ключевым словам",
              4: "Топ поисковых слов"}

    for key, value in action.items():
        print("{0}: {1}".format(key, value))
    choice_action = input("Choose an action: ")                                  # предложение выбора из главного меню

    match choice_action:                                                         # конструкция сравнения цифры пользователя с ключом из словаря action
        case "0":
            print("Work completed! By!")
            break
        case "1":                                                                # выбор по жанру и году
            functions.get_list_genres()                                          # направление в functions.get_list_genres список жанров
            genre = input("\n Выберите жанр: ")
            print(f"Вы выбрали - {genre}")
            save_list = [genre]
            functions.insert_db(save_list)                                       # запись в таблицу поисков
            choice = input("Выбрать год выпуска фильма? Y,N :").lower()
            year = ()
            if choice == 'y':
                year = input("Введите год(ы) через пробел: ").split()            # выбор года
                result = functions.search_genres_years(genre, *year)             # вызов функции поиска по жанру и году
            else:
                result = functions.search_genres_years(genre, *year)             # вызов функции поиска по жанру и году (год пустой)
            if result == 1:                                                      # ничего не найдено, повтор главного меню
                continue
            spisok_id = functions.print_result(result)                           # печать результата поиска
            print("")
            functions.search_id(spisok_id)                                       # функция поиска по id
            print("\n")
        case "2":                                                                # выбор по году
            genre = ""
            year = input("Введите год(ы) через пробел: ").split()
            if len(year) != 0:
                result = functions.search_genres_years(genre, *year)
                if result == 1:
                    continue
                spisok_id = functions.print_result(result)
                functions.search_id(spisok_id)
            else:
                print(f"Неправильно введен год, повторите.")
                continue
            print("\n")
        case "3":                                                                 # поиск по ключевым словам
            top_words = functions.top_words()
            print(f"Для поиска можете воспользоватся списком из топ 10:\n{' '.join(top_words)}\n"
                  f" или введите свои слова.")
            key_words = input("Введите слова для поиска через пробел: ")
            result = functions.search_key_words_title(key_words)
            ins_word = [key_words.split()]
            functions.insert_db(*ins_word)                                          # пополнение таблицы запросов
            spisok_id = functions.print_result(result)
            functions.search_id(spisok_id)
            print("\n")
        case "4":                                                                    # вывод списка ключевых слов
            words = functions.top_words()
            print(' '.join(words))
            print("\n")
        case _default:
            break
