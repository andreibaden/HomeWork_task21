from task21_v2.comp_v2 import *


class Count:
    def total_cost(comps):
        if not isinstance(comps, (list, tuple)):
            return Comp()

        sum = 0
        for i in comps:
            if isinstance(i, Comp):
                if i.get_price() >= 0:
                    sum += i.get_price()

        return sum

    def find_expensive(comps1):
        if not isinstance(comps1, (list, tuple)):
            return Comp()

        target1 = comps1[0]
        for i in comps1:
            if isinstance(i, Comp):
                if i.get_price() > 0:
                    if i.get_price() > target1.get_price():
                        target1 = i

        return target1

    def find_cheap(comps):
        if not isinstance(comps, (list, tuple)):
            return Comp()

        target2 = comps[0]
        for i in comps:
            if isinstance(i, Comp):
                if i.get_price() > 0:
                    if i.get_price() < target2.get_price():
                        target2 = i

        return target2


if __name__ == "__main__":
    lap1 = Comp()
    lap2 = Comp()
    lap3 = Comp()
    lap4 = Comp()

    lap1.set_brand("QWER")
    lap1.set_model("444")
    lap1.set_price(2000)

    lap2.set_brand("LG")
    lap2.set_model("9119")
    lap2.set_price(-1000)

    lap3.set_brand("Dell")
    lap3.set_model("789")
    lap3.set_price(300)

    lap4.set_brand("SAlE")
    lap4.set_model("7")
    lap4.set_price(-70000)

    lap_all = (lap1, lap2, lap3, lap4)

    total = Count.total_cost(lap_all)
    expensive = Count.find_expensive(lap_all)
    cheap = Count.find_cheap(lap_all)
    print("All prices:", lap1.get_price(), lap2.get_price(),
          lap3.get_price(), lap4.get_price())
    print("Total_cost         -->", total)
    print("Expensive computer -->", expensive)
    print("Cheap computer     -->", cheap)
