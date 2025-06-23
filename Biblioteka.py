from datetime import datetime, timedelta


class Material:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def get_info(self):
        return f"{self.title}, - {self.year}, - {self.author}"


class PrintedMaterial(Material):
    def __init__(self, title, year, author, isbn):
        super().__init__(title, year, author)
        self.isbn = isbn

    def get_info(self):
        return f"{self.title} - {self.year} - {self.author} - {self.isbn}"


class Film(Material):
    def __init__(self, title, year, author, time):
        super().__init__(title, year, author)
        self.time = time

    def get_info(self):
        return f"{self.title} - {self.year} - {self.author} - {self.time} min"


class Library:
    def __init__(self):
        self.materials = []
        self.borrowed_materials = []

    def add_material(self, material):
        self.materials.append(material)

    def list_all_materials(self):
        for material in self.materials:
            print(material.get_info())

    def list_all_materials_with_status(self):
        print("----- Niewypożyczone materiały -----")
        for material in self.materials:
            if isinstance(material, PrintedMaterial):
                print(material.get_info() + " (Książka)")
            elif isinstance(material, Film):
                print(material.get_info() + " (Film)")

        print("\n----- Wypożyczone materiały -----")
        for material, borrower, due_date in self.borrowed_materials:
            if isinstance(material, PrintedMaterial):
                print(material.get_info() + f" (Książka) - Wypożyczył(a): {borrower}, Data zwrotu: {due_date}")
            elif isinstance(material, Film):
                print(material.get_info() + f" (Film) - Wypożyczył(a): {borrower}, Data zwrotu: {due_date}")

    def list_borrowed_materials(self):
        for material, borrower, due_date in self.borrowed_materials:
            print(f"Tytuł: {material.title}, Wypożyczający: {borrower}, Data zwrotu: {due_date}")

    def borrow_material(self, material, borrower, a):
        if a<2:
            if a==0:
                day=35
            else:
                day =45
            if material in self.materials:
                due_date = datetime.now() + timedelta(days=day)
                self.borrowed_materials.append((material, borrower, due_date))
                self.materials.remove(material)
                print(f"{borrower} wypożyczył(a) {material.title}. Proszę zwrócić do {due_date}.")
            else:
                print("Materiał niedostępny w bibliotece.")
        else:
            print("Ta osoba nie ma uprawnień do wypożyczenia")

    def list_borrowed(self):
        print("Książki: ")
        for material, borrower, due_date in self.borrowed_materials:
            if isinstance(material, PrintedMaterial):
                print(f"{material.title}, Wypożyczający: {borrower}, Data zwrotu: {due_date}")

        print("Filmy:")
        for material, borrower, due_date in self.borrowed_materials:
            if isinstance(material, Film):
                print(f"{material.title}, Wypożyczający: {borrower}, Data zwrotu: {due_date}")
        print("")
    def return_material(self, material, borrower, a):
        for item in self.borrowed_materials:
            if item[0] == material and item[1] == borrower and (a==0 or a==1):
                self.borrowed_materials.remove(item)
                self.materials.append(material)
                print(f"{borrower} zwrócił(a) {material.title}.")
                return
        print(f"{borrower} nie wypożyczył(a) {material.title}.")

    def remove_material(self, material):
        if material in self.materials:
            self.materials.remove(material)
            print(f"{material.title} został(a) usunięty(a) ze zbiorów biblioteki.")
        else:
            print(f"{material.title} nie istnieje w zbiorach biblioteki.")

library = Library()

# Uzupełnianie biblioteki
book1 = PrintedMaterial("Na przekór nocy", 2022, "Brigid Kemmerer", "9788381789936")
library.add_material(book1)
book2 = PrintedMaterial("Harry Potter i Kamień Filozoficzny", 1997, "J.K. Rowling", "9780747532699")
library.add_material(book2)
book3 = PrintedMaterial("W ramionach gwiazd", 2016, "Amie Kaufman, Megan Spooner", "9788375151008")
library.add_material(book3)
book4 = PrintedMaterial("Utkane królestwo", 2023, "Tahereh Mafi", "9788367551601")
library.add_material(book4)
film1 = Film("Incepcja", 2010, "Christopher Nolan", 148)
library.add_material(film1)
film2 = Film("Pan i Pani Smith", 2014, "Christopher Nolan", 169)
library.add_material(film2)
film3 = Film("Narzeczony mimo woli", 2010, "Christopher Nolan", 148)
library.add_material(film3)
film4 = Film("Nie wierzcie bliźniaczką", 2014, "Christopher Nolan", 169)
library.add_material(film4)


# Zawartosc biblioteki
print("Biblioteka:")
print(" ")
library.list_all_materials()
print(" ")

# Wypożyczanie materiałów
print("Wypożyczenia: ")
print(" ")
library.borrow_material(book1, "Ala Nowak", 0)
library.borrow_material(film1, "Bartek Jan", 1)
library.borrow_material(film2, "Klara Korybut", 2)
library.borrow_material(book3, "Ala Nowak", 0)
library.borrow_material(film4, "Filip Nowak", 1)
print(" ")

#Lista wypożyczonych materiałów
print("Wypożyczone zasoby:")
print(" ")
library.list_borrowed()
print(" ")

# Zwracanie materiałów
print("Zwroty: ")
print(" ")
library.return_material(book1, "Ala Nowak", 0)
library.return_material(film2, "Ala Nowak", 0)
library.return_material(book2, "Ala Nowak", 0)
print(" ")

#usuwanie pozycji ze zbioru biblioteki
print("Pozycje usunięte: ")
print(" ")
library.remove_material(book1)
print(" ")

#materiały na stanie biblioteki
print("Stan aktualny biblioteki: ")
print(" ")
library.list_all_materials_with_status()