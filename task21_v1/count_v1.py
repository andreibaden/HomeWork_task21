from comp_v1 import *


class Count:
    def total_cost(comps):
        if not isinstance(comps, (list, tuple)):
            return Comp()

        sum = 0
        for i in comps:
            if isinstance(i, Comp):
                if i.price >= 0:
                    sum += i.price

        return sum

    def find_expensive(comps1):
        if not isinstance(comps1, (list, tuple)):
            return Comp()

        target1 = comps1[0]
        for i in comps1:
            if isinstance(i, Comp):
                if i.price >= 0:
                    if i.price > target1.price:
                        target1 = i
        # if target1.price < 0:
        #     target1.price = "Error! Price is less than zero!"

        return target1

    def find_cheap(comps2):
        if not isinstance(comps2, (list, tuple)):
            return Comp()

        target2 = comps2[0]
        for i in comps2:
            if isinstance(i, Comp):
                if i.price >= 0:
                    if i.price < target2.price:
                        target2 = i
        if target2.price < 0:
            target2.price = "Error! Price is less than zero!"

        return target2

if __name__ == "__main__":
    laptop1 = Comp("LG", "111", 900)
    laptop2 = Comp("Anna", "222", -500)
    laptop3 = Comp("Dell", "333", 200)
    laptop4 = Comp("Kuocera", "444", -90)
    laptop5 = Comp("Alisa", "555", -50)
    laptop6 = Comp("Enot", "666", -20)

    laptop_123 = (laptop1, laptop2, laptop3)
    telik_456 = (laptop4, laptop5, laptop6)

    total_123 = Count.total_cost(laptop_123)
    expensive_123 = Count.find_expensive(laptop_123)
    cheap_123 = Count.find_cheap(laptop_123)

    total_456 = Count.total_cost(telik_456)
    expensive_456 = Count.find_expensive(telik_456)
    cheap_456 = Count.find_cheap(telik_456)

    print("Total_cost 123         -->", total_123)
    print("Expensive computer 123 -->", expensive_123)
    print("Cheap computer 123     -->", cheap_123)
    print("\nTotal_cost 456            -->", total_456)
    print("Expensive computer 456    -->", expensive_456)
    print("Cheap computer 456        -->", cheap_456)
