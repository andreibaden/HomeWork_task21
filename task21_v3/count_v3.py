from task21_v3.comp_v3 import *


class Count:
    def total_cost(self):
        if not isinstance(self, (list, tuple)):
            return Comp()

        sum = 0
        for i in self:
            if isinstance(i, Comp):
                if i.price >= 0:
                    sum += i.price

        return sum

    def find_expensive(self):
        if not isinstance(self, (list, tuple)):
            return Comp()

        target1 = self[0]
        for i in self:
            if isinstance(i, Comp):
                if i.price > 0:
                    if i.price > target1.price:
                        target1 = i

        return target1

    def find_cheap(self):
        if not isinstance(self, (list, tuple)):
            return Comp()

        target2 = self[0]
        for i in self:
            if isinstance(i, Comp):
                if i.price > 0:
                    if i.price < target2.price:
                        target2 = i

        return target2


if __name__ == "__main__":
    lap1 = Comp("QWER", "444", 2000)
    lap2 = Comp("LG", "9119", -1000)
    lap3 = Comp("Dell", "789", 300)
    lap4 = Comp("SAlE", "7", -70000)

    lap_all = (lap1, lap2, lap3, lap4)

    total = Count.total_cost(lap_all)
    expensive = Count.find_expensive(lap_all)
    cheap = Count.find_cheap(lap_all)
    print("All prices:", lap1.price, lap2.price,
          lap3.price, lap4.price)
    print("Total_cost         -->", total)
    print("Expensive computer -->", expensive)
    print("Cheap computer     -->", cheap)
