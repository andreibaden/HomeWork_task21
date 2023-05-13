class Comp:
    def __init__(self, brand="no brand", model="no model", price=0):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def get_brand(self):
        return self.__brand

    def set_brand(self, name):
        self.__brand = name

    def get_model(self):
        return self.__model

    def set_model(self, name):
        self.__model = name

    def get_price(self):
        return self.__price

    def set_price(self, name):
        if name >= 0:
            self.__price = name

    def __str__(self):
        return f"computer: {self.__brand}, model _ {self.__model}, " \
               f"price = {self.__price} rub."


if __name__ == "__main__":
    laptop1 = Comp()
    print(laptop1)

    lap2 = Comp()
    lap2.set_brand("LG")
    lap2.set_model("9119")
    lap2.set_price(-200)
    print("laptop2 -->", lap2.get_brand(), lap2.get_model(), lap2.get_price())

    lap3 = Comp()
    lap3.set_brand("DELL")
    lap3.set_price(11100)
    print("laptop3 -->", lap3.get_brand(), lap3.get_model(), lap3.get_price())
