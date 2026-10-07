class Human:
    # Constructor to initialize the attributes
    def __init__(self, full_name="", birth_date="", phone="", city="", country="", address=""):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    # Method to input data from the keyboard
    def input_data(self):
        print("--- Введення даних про людину ---")
        self.full_name = input("Введіть ПІБ: ")
        self.birth_date = input("Введіть дату народження (напр. 15.05.1990): ")
        self.phone = input("Введіть контактний телефон: ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.address = input("Введіть домашню адресу: ")

    # Method to display all data
    def display_data(self):
        print("\n=== Інформація про людину ===")
        print(f"ПІБ:             {self.full_name}")
        print(f"Дата народження: {self.birth_date}")
        print(f"Телефон:         {self.phone}")
        print(f"Країна:          {self.country}")
        print(f"Місто:           {self.city}")
        print(f"Домашня адреса:  {self.address}")
        print("=============================\n")

    # Additional operation: updating the phone number
    def set_phone(self, new_phone):
        self.phone = new_phone
        print(f"[Успішно] Номер телефону для {self.full_name} змінено на {self.phone}")

    # Additional operation: getting a short location string
    def get_location(self):
        return f"{self.city}, {self.country}"


# ==========================================
# Приклад використання класу (тестування)
# ==========================================

# 1. Створюємо порожній об'єкт людини
person1 = Human()

# 2. Викликаємо метод для заповнення даних з клавіатури
person1.input_data()

# 3. Виводимо введені дані на екран
person1.display_data()

# 4. Демонстрація роботи додаткових методів
person1.set_phone("+380991234567")
print(f"Коротка локація: {person1.get_location()}")

# Перевіряємо, чи змінився телефон
person1.display_data()