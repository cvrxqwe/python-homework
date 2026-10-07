class City:
    # Конструктор класу (шаблон з порожніми або базовими значеннями)
    def __init__(self, name="", region="", country="", population=0, postal_code="", phone_code=""):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    # Метод для заповнення даних з клавіатури
    def input_data(self):
        print("--- Введення даних про місто ---")
        self.name = input("Введіть назву міста: ")
        self.region = input("Введіть назву регіону/області: ")
        self.country = input("Введіть назву країни: ")

        # Тут ми згадуємо тему "Винятки" (Exceptions), яку розбирали раніше
        while True:
            try:
                self.population = int(input("Введіть кількість жителів (лише цифри): "))
                if self.population < 0:
                    print("Населення не може бути від'ємним. Спробуйте ще раз.")
                    continue
                break  # Якщо все правильно, виходимо з циклу
            except ValueError:
                print("Помилка! Потрібно ввести ціле число.")

        self.postal_code = input("Введіть поштовий індекс: ")
        self.phone_code = input("Введіть телефонний код: ")

    # Метод для красивого виведення інформації на екран
    def display_data(self):
        print("\n=== Інформація про місто ===")
        print(f"Місто:           {self.name}")
        print(f"Регіон:          {self.region}")
        print(f"Країна:          {self.country}")
        print(f"Населення:       {self.population} осіб")
        print(f"Поштовий індекс: {self.postal_code}")
        print(f"Телефонний код:  {self.phone_code}")
        print("============================\n")

    # Додаткова операція 1: Оновлення кількості населення (наприклад, після перепису)
    def update_population(self, new_population):
        if new_population >= 0:
            self.population = new_population
            print(f"[Успішно] Населення міста {self.name} оновлено: {self.population} осіб.")
        else:
            print("[Помилка] Населення не може бути від'ємним.")

    # Додаткова операція 2: Швидке отримання повної геолокації рядком
    def get_full_location(self):
        return f"{self.name} ({self.region}, {self.country})"


# ==========================================
# Тестування класу
# ==========================================

# 1. Створюємо порожній об'єкт міста
my_city = City()

# 2. Заповнюємо його даними (програма попросить ввести їх у консолі)
my_city.input_data()

# 3. Виводимо на екран
my_city.display_data()

# 4. Перевіряємо додаткові методи
print(f"Коротка інформація: {my_city.get_full_location()}")
my_city.update_population(300000)