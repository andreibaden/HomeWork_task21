from comp import *


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


    def find_expensive(comps):
        if not isinstance(comps, (list, tuple)):
            return Comp()

        target = comps[0]
        for i in comps:
            if isinstance(i, Comp):
                if i.price > 0 and i.price > 0:
                    if i.price > target.price:
                        target = i

        return target

    def find_cheap(comps):
        if not isinstance(comps, (list, tuple)):
            return Comp()

        target = comps[0]
        for i in comps:
            if isinstance(i, Comp):
                if i.price > 0 and i.price > 0:
                    if i.price < target.price:
                         target = i

        return target


if __name__ == "__main__":
    laptop1 = Comp("LG", "9119", 100)
    laptop2 = Comp("Anna", "Daf", -550)
    laptop3 = Comp("Dell", "789", 200)

    laptop_123 = (laptop1, laptop2, laptop3)

    total_123 = Count.total_cost(laptop_123)
    expensive_123 = Count.find_expensive(laptop_123)
    cheap_123 = Count.find_cheap(laptop_123)

    print("Total_cost -->", total_123)
    print("Expensive computer -->", expensive_123)
    print("Cheap computer -->", cheap_123)
