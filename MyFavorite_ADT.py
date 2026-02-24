#IMPLEMENTASI MENGGUNAKAN ADT
class MyFavorite:
    def __init__(self, name, food, drink):
        self.__name = name
        self.__food = food
        self.__drink = drink

    def favorite_self(self):
        print(f"Hello, my name is {self.__name}, "
              f"my favorite food is {self.__food}, "
              f"my favorite drink is {self.__drink}")

    def change_drink(self, new_drink):
        self.__drink = new_drink
        print(f"My new favorite drink is {self.__drink}")

    # Getter (opsional, agar tetap terkontrol)
    def get_name(self):
        return self.__name

    def get_food(self):
        return self.__food

    def get_drink(self):
        return self.__drink


# Contoh penggunaan ADT
favoriteOne = MyFavorite("Dina", "soto", "kopi")
favoriteTwo = MyFavorite("Lauren", "nasi goreng", "teh")
favoriteThree = MyFavorite("Yaya", "sup", "jus")

favoriteOne.favorite_self()
favoriteOne.change_drink("susu")
favoriteOne.favorite_self()


#IMPLEMENTASI TANPA ADT
class MyFavorite:
    def __init__(self, name, food, drink):
        self.name = name
        self.food = food
        self.drink = drink


# Contoh penggunaan tanpa ADT
favoriteOne = MyFavorite("Dina", "soto", "kopi")

print(favoriteOne.name)
print(favoriteOne.food)
print(favoriteOne.drink)

# Data bisa diubah langsung (tanpa kontrol)
favoriteOne.drink = "susu"
print("Minuman baru:", favoriteOne.drink)

