import json

# Загрузка данных из JSON
def load_data():
    with open("astronomy_data.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Двухмерный список с данными, где:
# 0 — ключевое слово, 1 — описание
data = load_data()

while True:
    query = input("Введите запрос: ").strip().lower()
    if query == 'exit' or query == 'выход':  # Прекращение работы цикла
        print("Выход из программы.")
        break

    # Поиск информации
    if_found = False  # Флаг для проверки наличия совпадений
    for item in data:
        if query in item[0].lower():  # Поиск подстроки, нечувствительный к регистру
            if_found = True
            print(f"{item[0]}: {item[1]}")

    if not if_found:
        print(f"Информация о '{query}' не найдена.")
print("Работа программы завершена")
