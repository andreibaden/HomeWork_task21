# Task 21 "Computer"
#
# Version: 1.0
# Author: Nedaboi Andrei_QA2023
# Date: 10.05.2023

from task21_v2.count_v2 import *


def main():
    computer1 = Comp("Lenovo", "Dragon", 200)
    computer2 = Comp("LG", "Ligi-88", 300)
    computer3 = Comp("Lampa", "Running", -100)
    computer4 = Comp("Lampa", "Running", 400)

    computers = ((computer1), (computer2), (computer3), (computer4))

    total = Count.total_cost(computers)
    expensive_comp = Count.find_expensive(computers)
    cheap_comp = Count.find_cheap(computers)

    print(f" Total cost all computers is {total} rub."
          f"\n Most expensive computer is {expensive_comp}"
          f"\n Most cheap computer is {cheap_comp}")


if __name__ == '__main__':
    main()
