class MyFavorite:
    def __init__(self, name, food, drink):
     self.name = name
     self.food = food
     self.drink = drink

    def favorite_self (self):
     print(f"Hello, my name is {self.name}, my favorite food is {self.food} , my favorite drink is {self.drink}")

    def change_drink(self,new_drink):
      self.drink = new_drink
      print(f"my new drink is {self.drink}")

favoriteOne = MyFavorite ("Dina", "soto", "kopi")
favoriteTwo = MyFavorite ("lauren", "nasi goreng", "teh")
favoriteThree = MyFavorite ("yaya", "sup", "jus")

print(favoriteOne.name)
print(favoriteOne.food)
favoriteOne.favorite_self()
favoriteOne.change_drink("susu")
favoriteOne.favorite_self()
