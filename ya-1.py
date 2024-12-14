import math

class Contact:
    def __init__(self, name, phone, birthday, address):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        print(f"Создаем новый контакт {name}")
    def show(self):
        print(f"Имя: {self.name}, телефон: {self.phone}, дата рождения: "
              f"{self.birthday}, "
              f"адрес: {self.address}")

    def __str__(self):
        return "Contact - " +self.name


mike = Contact("Михаил Булгаков", "4-5-77", "15.01.1922", "Россия, г.Москва, ул. Веселая, д.15 кв.23")
vlad = Contact("Владимир Маяковский", "41-25-77", "25.08.1902", "Россия, "
                                                            "г.Москва, "
                                                       "ул. Грустная, "
                                                                "д.15 кв.23")


mike.address = "Россия, г.Москва, ул. Абрикосовая, д.1 кв.60"
mike.phone = "977-999-34"

vlad.phone = "965-65-65"

vlad.show()

print(mike)

class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = 4 * math.pi * radius * radius
        self.average_temp_celsius = temp_celsius
        self.average_temp_fahrenheit = 9 / 5 * temp_celsius +32


    def show_info(self):
        print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} "
              f"кв.км.")
        print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit} градусов "
              f"по "
              f"Фаренгейту")


jupiter = Planet('Юпитер', 69911, -108)

jupiter.show_info()