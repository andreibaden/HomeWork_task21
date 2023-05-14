class Comp:
    def __init__(self, brand="no brand", model="no model", price=0):
        self.__brand = brand
        self.__model = model
        self.__price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, name):
        self.__brand = name

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, name):
        self.__model = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, name):
        if name >= 0:
            self.__price = name

    def __str__(self):
        return f"computer: {self.__brand}, model {self.__model}, " \
               f"price = {self.__price} rub."


if __name__ == "__main__":
    laptop1 = Comp()
    print(laptop1)

    lap2 = Comp()
    lap2.brand = "LG"
    lap2.model = "9119"
    lap2.price = 200
    print("lap2 -->", lap2.brand, lap2.model, lap2.price)

    lap3 = Comp("DELL", "Strong", -1000)
    print("lap3 -->", lap3.brand, lap3.model, lap3.price)
