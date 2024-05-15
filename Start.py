import functions


start_text1 = "Привет! Мы поможем вам найти интересный фильм, чтобы провести вечер не сучно!"
start_text2 = "В нашей базе более 5500 фильмов по 23 жанрам. Удачного поиска!"
start_text3 = "@2024"

print("\n", start_text1.center(100), "\n", start_text2.center(100))
print(start_text3.center(100))

while True:
    action = {0: "Exit", 1: "Поиск по жанру", 2: "Поиск по году", 3: "Поиск по ключевым словам",
              4: "Selection by criteria"}

    for key, value in action.items():
        print("{0}: {1}".format(key, value))
    choice_action = input("Choose an action: ")

    match choice_action:
        case "0":
            print("Work completed! By!")
            break
        case "1":
            functions.get_list_genres()
            gener = input("\n Выберите жанр: ").strip()
            print(f"Вы выбрали - {gener}")
            result = functions.search_genres(gener)
            functions.print_result(result)
            print("Action completed ", "\n")
        case "2":
#            dbconnect = DbSql()
#            search_year
            print("Action completed ", "\n")
        case "3":
#            dbconnect = DbSql()
#            search_keyword()
            print("Action completed ", "\n")
        case _default:
            break
