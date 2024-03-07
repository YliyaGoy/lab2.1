#существует соглашение о том, что поля и методы, которые начинаются с одного символа подчеркивания (например, _), считаются "protected" (защищенными), и их следует рассматривать как вутренние для класса.
# Поля или методы, которые начинаются с двух символов подчеркивания (например, __variable), считаются "private" (приватными)

class Room:
    def __init__(self, area=0, height=0, style="modern"):
        # Конструктор класса Room
        self.area = area  # Поле площади комнаты
        self.height = height  # Поле высоты комнаты
        self.style = style  # Поле стиля комнаты

    def __del__(self):
        # Деструктор класса Room
        print("Комната уничтожена")

    def get_area(self): # получение значения
        return self.area

    def get_height(self):# получение значения
        return self.height

    def get_style(self):# получение значения
        return self.style

    def set_area(self, area): # установка значения
        self.area = area

    def set_style(self, style): # установка значения
        self.style = style

    def set_height(self, height):# установка значения
        self.height = height

    def copy(self): # метод для вывода информации
        print(f"Площадь: {self.get_area()} ")
        print(f"Высота: {self.get_area()}")
        print(f"Стиль комнаты: {self.get_style()}")

    def __private_method(self): # метод для вычисления удвоенной длины одного измерения комнаты (обычно длины или ширины)
        print("Удвоенная длина одного измерения комнаты (длины или ширины):")
        per = self.get_area() / self.get_height()
        print(per)

    def public_method(self): # вызывает приватный метод, который считает периметр
        print("Это публичный метод, вызывающий приватный метод:")
        self.__private_method()


class OneRoomFlat(Room):
    def __init__(self, area, height, style, kitchen_area, floor):
        # Конструктор класса
        super().__init__(area, height, style)
        self.kitchen_area = kitchen_area
        self.floor = floor

    def get_floor(self): # получение значения
        return self.floor

    def get_room_area(self): # получение значения
        return self.area

    def get_kitchen_area(self): # получение значения
        return self.kitchen_area

    def set_floor(self,floor): # установка значения
        self.floor = floor

    def set_room_area(self,area): # установка значения
        self.area = area

    def set_kitchen_area(self,kitchen_area): # установка значения
        self.kitchen_area = kitchen_area

    def copy_studio(self): # метод для вывода информации
        print(f"Площадь квартиры: {self.get_room_area()} ")
        print(f"Этаж: {self.get_floor()}")
        print(f"Площадь кухни: {self.kitchen_area()}")


class PublicOneRoomFlat(OneRoomFlat):
    def __init__(self,  kitchen_area, floor, city_name,area, height, style): # конструктор
        super().__init__(area, height, style, kitchen_area, floor)
        self.city_name = city_name

    def get_floor(self):  # получение значения
        return self.floor

    def get_room_area(self):  # получение значения
        return self.area

    def get_kitchen_area(self):  # получение значения
        return self.kitchen_area

    def get_city_name(self):  # получение значения
        return self.city_name

    def print_details(self):
        # Метод для печати
        print(f"Город: {self.city_name}, Этаж: {self.floor}, Площадь комнаты: {self.get_room_area()}, Площадь кухни: {self.get_kitchen_area()}")

    def set_floor(self, floor): # установка значения
        self.floor = floor

    def set_room_area(self, area): # установка значения
        self.area = area

    def set_kitchen_area(self, kitchen_area): # установка значения
        self.kitchen_area = kitchen_area

    def set_city_name(self, city_name): # установка значения
        self.city_name = city_name


class _StudioApartment(Room):
    def __init__(self, kitchen_area, floor, studio_name,area, height, style):
        # Конструктор класса
        super().__init__(area, height, style)
        self.kitchen_area = kitchen_area
        self.floor = floor
        self.studio_name = studio_name

    def get_floor(self): # получение значения
        return self.floor

    def get_room_area(self): # получение значения
        return self.area

    def get_kitchen_area(self): # получение значения
        return self.kitchen_area

    def get_studio_name(self): # получение значения
        return self.studio_name

    def set_floor(self, floor): # установка значения
        self.floor = floor

    def set_room_area(self, area): # установка значения
        self.area = area

    def set_kitchen_area(self, kitchen_area): # установка значения
        self.kitchen_area = kitchen_area

    def set_studio_name(self, studio_name): # установка значения
        self.studio_name = studio_name

    def copy_studio(self): # метод для вывода информации
        print(f"Площадь: {self.get_room_area()} ")
        print(f"Название: {self.get_studio_name()}")
        print(f"Этаж: {self.get_floor()}")
        print(f"Площадь кухни: {self.kitchen_area()}")


def room_menu(room_obj): # меню для работы с комнатой
    while True:
        print("\n-------Меню для работы с комнатой-------")
        print("1. Получить площадь комнаты")
        print("2. Получить высоту комнаты")
        print("3. Получить стиль комнаты")
        print("4. Установить площадь комнаты")
        print("5. Установить стиль комнаты")
        print("6. Установить высоту комнаты")
        print("7. Вывести площадь комнаты, высоту комнаты и стиль комнаты")
        print("8. Удвоенная длина одного измерения комнаты (длины или ширины)")
        print("9. Назад в главное меню")
        choice = int(input("Выберите действие: "))

        if choice == 1:
            print(f"Площадь комнаты: {room_obj.get_area()}")
        elif choice == 2:
            print(f"Высота комнаты: {room_obj.get_height()}")
        elif choice == 3:
            print(f"Стиль комнаты: {room_obj.get_style()}")
        elif choice == 4:
            new_area = float(input("Введите новую площадь комнаты: "))
            room_obj.set_area(new_area)
        elif choice == 5:
            new_style = input("Введите новый стиль комнаты: ")
            room_obj.set_style(new_style)
        elif choice == 6:
            new_height = float(input("Введите новую высоту комнаты: "))
            room_obj.set_height(new_height)
        elif choice == 7:
            room_obj.copy()
        elif choice == 8:
            room_obj.public_method()
        elif choice == 9:
            break


def studio_menu(studio_obj): # меню для работы со студией
    while True:
        print("\n-------Меню для работы со студией-------")
        print("1. Площадь студии")
        print("2. Этаж")
        print("3. Имя студии")
        print("4. Площадь кухни")
        print("5. Установить площадь студии")
        print("6. Установить имя студии")
        print("7. Установить этаж")
        print("8. Установить площадь кухни")
        print("9. Вывести детали о студии")
        print("10. Назад в главное меню")
        choice = int(input("Выберите действие: "))

        if choice == 1:
            print(f"Площадь студии: {studio_obj.get_area()}")
        elif choice == 2:
            print(f"Этаж: {studio_obj.get_floor()}")
        elif choice == 3:
            print(f"Имя студии: {studio_obj.get_studio_name()}")
        elif choice == 4:
            print(f"Площадь кухни: {studio_obj.get_kitchen_area()}")
        elif choice == 5:
            new_area = float(input("Введите новую площадь студии: "))
            studio_obj.room_area(new_area)
        elif choice == 6:
            new_name = input("Введите новое имя студии: ")
            studio_obj.set_studio_name(new_name)
        elif choice == 7:
            new_name = input("Введите этаж студии: ")
            studio_obj.set_floor(new_name)
        elif choice == 8:
            kitchen_area = float(input("Введите новую площадь кухни: "))
            studio_obj.set_kitchen_area(kitchen_area)
        elif choice == 9:
            studio_obj.copy_studio()
        elif choice == 10:
            break


def flat_menu(flat_obj): # меню для работы с однокомнатной квартирой
    while True:
        print("\n-------Меню для работы с однокомнатной квартирой-------")
        print("1. Площадь комнаты")
        print("2. Площадь кухни")
        print("3. Этаж")
        print("4. Город")
        print("5. Установить площадь комнаты")
        print("6. Установить площадь кухни")
        print("7. Установить этаж")
        print("8. Установить город")
        print("9. Вывести детали о квартире")
        print("10. Назад в главное меню")
        choice = int(input("Выберите действие:"))

        if choice == 1:
            print(f"Площадь комнаты: {flat_obj.get_room_area()}")
        elif choice == 2:
            print(f"Площадь кухни: {flat_obj.get_kitchen_area()}")
        elif choice == 3:
            print(f"Этаж: {flat_obj.get_floor()}")
        elif choice == 4:
            print(f"Город: {flat_obj.get_city_name()}")
        elif choice == 5:
            new_area = float(input("Введите новую площадь комнаты: "))
            flat_obj.set_room_area(new_area)
        elif choice == 6:
            new_kitchen_area = float(input("Введите новую площадь кухни: "))
            flat_obj.set_kitchen_area(new_kitchen_area)
        elif choice == 7:
            new_floor = int(input("Введите новый этаж: "))
            flat_obj.set_floor(new_floor)
        elif choice == 8:
            new_city = int(input("Введите новый город: "))
            flat_obj.set_city_name(new_city)
        elif choice == 9:
            flat_obj.print_details()
        elif choice == 10:
            break


def main(): # основной метод вызова
    room1 = Room(50.0, 3.5, 'модерн')
    flat = PublicOneRoomFlat(room1, 15.0, 2, 'Нью-Йорк')
    studio1 = _StudioApartment(room1, 12.0, 3, "Арт-студия")

    while True:
        print("\n-------Главное меню-------")
        print("1. Работать с комнатой")
        print("2. Работать со студией")
        print("3. Работать со однокомнатной крвартирой")
        print("4. Выход")
        choice = int(input("Выберите объект для работы: "))

        if choice == 1:
            room_menu(room1)
        elif choice == 2:
            studio_menu(studio1)
        elif choice == 2:
            flat_menu(flat)
        elif choice == 4:
            print("Выход")
            break


if __name__ == "__main__":
    main()