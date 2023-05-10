class Comp:
    def __init__(self, brand="no brand", model="no model", price=0):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"computer: {self.brand}, model _ {self.model}, " \
            f"price = {self.price} rub."

if __name__ == "__main__":
    laptop1 = Comp()
    print(laptop1)

    laptop2 = Comp("LG", "9119", 2000)
    print(laptop2)

    laptop3 = Comp()
    laptop3.brand = "DELL"
    # laptop.model = "Fly"
    laptop3.price = 11100
    print(laptop3)