#food
class KenyanFood:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def describe(self):
        return self.name + " is made with " + ", ".join(self.ingredients) + " and costs KES " + str(self.price)

    def serve(self):
        return "Serving " + self.name + " hot and fresh!"


class LocalDish(KenyanFood):
    def __init__(self, name, ingredients, price, is_vegetarian):
        super().__init__(name, ingredients, price)
        self.is_vegetarian = is_vegetarian


    def serve(self):
        if self.is_vegetarian:
            return "Enjoy your vegetarian " + self.name
        else:
            return "Enjoy your " + self.name + " with nyama choma"


#beverages
class Beverage(KenyanFood):
    def __init__(self, name, ingredients, price, is_hot):
        super().__init__(name, ingredients, price)
        self.is_hot = is_hot


    def describe(self):
        if self.is_hot:
            temp = "hot"
        else:
            temp = "cold"
        return self.name + " is a " + temp + " drink made with " + ", ".join(self.ingredients) + ". Price: KES " + str(self.price)


#examples
ugali = LocalDish("Ugali", ["maize flour", "water"], 50, True)
pilau = LocalDish("Pilau", ["rice", "beef", "spices"], 150, False)
chai = Beverage("Chai", ["tea leaves", "milk", "sugar"], 30, True)
mursik = Beverage("Mursik", ["fermented milk"], 60, False)


print(ugali.describe())
print(ugali.serve())
print(pilau.describe())
print(pilau.serve())
print(chai.describe())
print(chai.serve())
print(mursik.describe())
print(mursik.serve())
