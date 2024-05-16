import functions

start_text1 = "Привет! Мы поможем вам найти интересный фильм, чтобы провести вечер не сучно!"
start_text2 = "В нашей базе более 5500 фильмов по 23 жанрам. Удачного поиска!"
start_text3 = "@2024"

print("\n", start_text1.center(100), "\n", start_text2.center(100))
print(start_text3.center(100))

while True:
    action = {0: "Exit", 1: "Поиск по жанру и году", 2: "Поиск по году", 3: "Поиск по ключевым словам",
              4: "Топ поисковых слов"}

    for key, value in action.items():
        print("{0}: {1}".format(key, value))
    choice_action = input("Choose an action: ")

    match choice_action:
        case "0":
            print("Work completed! By!")
            break
        case "1":
            functions.get_list_genres()
            genre = input("\n Выберите жанр: ")
            print(f"Вы выбрали - {genre}")
            choice = input("Выбрать год выпуска фильма? Y,N :")
            year = ()
            if choice == 'Y'or choice == 'y':
                year = input("Введите год(ы) через пробел: ").split()
                result = functions.search_genres_years(genre,*year)
            else:
                result = functions.search_genres_years(genre,*year)
            if result == 1:
                continue
            spisok_id = functions.print_result(result)
            print("")
            functions.search_id(spisok_id)
            print("\n")
        case "2":
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
        case "3":
            key_words = input("Введите слова для поиска через пробел: ")
            result = functions.search_key_words_title(key_words)
            spisok_id = functions.print_result(result)
            functions.search_id(spisok_id)
            print("\n")
        case "4":
            print("\n")
        case _default:
            break
