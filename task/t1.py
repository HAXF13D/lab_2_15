#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money:

    def __init__(
            self,
            penny_1=0,
            penny_5=0,
            penny_10=0,
            penny_50=0,
            ruble_1=0,
            ruble_2=0,
            ruble_5=0,
            ruble_10=0,
            ruble_50=0,
            ruble_100=0,
            ruble_200=0,
            ruble_500=0,
            ruble_1000=0,
            ruble_2000=0,
            ruble_5000=0
    ):
        self.__penny_1 = int(penny_1)
        self.__penny_5 = int(penny_5)
        self.__penny_10 = int(penny_10)
        self.__penny_50 = int(penny_50)

        self.__ruble_1 = int(ruble_1)
        self.__ruble_2 = int(ruble_2)
        self.__ruble_5 = int(ruble_5)
        self.__ruble_10 = int(ruble_10)
        self.__ruble_50 = int(ruble_50)
        self.__ruble_100 = int(ruble_100)
        self.__ruble_200 = int(ruble_200)
        self.__ruble_500 = int(ruble_500)
        self.__ruble_1000 = int(ruble_1000)
        self.__ruble_2000 = int(ruble_2000)
        self.__ruble_5000 = int(ruble_5000)

        self.__set_summa()

    def __del__(self):
        print(f"{self.summa} удалено")

    def __str__(self):
        return f"{self.summa}"



    @property
    def penny_1(self):
        return self.__penny_1

    @property
    def penny_5(self):
        return self.__penny_5

    @property
    def penny_10(self):
        return self.__penny_10

    @property
    def penny_50(self):
        return self.__penny_50

    @property
    def ruble_1(self):
        return self.__ruble_1

    @property
    def ruble_2(self):
        return self.__ruble_2

    @property
    def ruble_5(self):
        return self.__ruble_5

    @property
    def ruble_10(self):
        return self.__ruble_10

    @property
    def ruble_50(self):
        return self.__ruble_50

    @property
    def ruble_100(self):
        return self.__ruble_100

    @property
    def ruble_200(self):
        return self.__ruble_200

    @property
    def ruble_500(self):
        return self.__ruble_500

    @property
    def ruble_1000(self):
        return self.__ruble_1000

    @property
    def ruble_2000(self):
        return self.__ruble_2000

    @property
    def ruble_5000(self):
        return self.__ruble_5000

    @property
    def summa(self):
        return self.__summa

    def __set_summa(self):
        summa = \
            self.penny_1 * 0.01 + \
            self.penny_5 * 0.05 + \
            self.penny_10 * 0.1 + \
            self.penny_50 * 0.5 + \
            self.ruble_1 * 1 + \
            self.ruble_2 * 2 + \
            self.ruble_5 * 5 + \
            self.ruble_10 * 10 + \
            self.ruble_50 * 50 + \
            self.ruble_100 * 100 + \
            self.ruble_200 * 200 + \
            self.ruble_500 * 500 + \
            self.ruble_1000 * 1000 + \
            self.ruble_2000 * 2000 + \
            self.ruble_5000 * 5000
        self.__summa = float(summa)

    def change_amount(
            self,
            penny_1=-1,
            penny_5=-1,
            penny_10=-1,
            penny_50=-1,
            ruble_1=-1,
            ruble_2=-1,
            ruble_5=-1,
            ruble_10=-1,
            ruble_50=-1,
            ruble_100=-1,
            ruble_200=-1,
            ruble_500=-1,
            ruble_1000=-1,
            ruble_2000=-1,
            ruble_5000=-1
    ):
        if penny_1 > 0:
            self.__penny_1 = penny_1
        if penny_5 > 0:
            self.__penny_5 = penny_5
        if penny_10 > 0:
            self.__penny_10 = penny_10
        if penny_50 > 0:
            self.__penny_50 = penny_50

        if ruble_1 > 0:
            self.__ruble_1 = ruble_1
        if ruble_2 > 0:
            self.__ruble_2 = ruble_2
        if ruble_5 > 0:
            self.__ruble_5 = ruble_5
        if ruble_10 > 0:
            self.__ruble_10 = ruble_10
        if ruble_50 > 0:
            self.__ruble_50 = ruble_50
        if ruble_100 > 0:
            self.__ruble_100 = ruble_100
        if ruble_200 > 0:
            self.__ruble_200 = ruble_200
        if ruble_500 > 0:
            self.__ruble_500 = ruble_500
        if ruble_1000 > 0:
            self.__ruble_1000 = ruble_1000
        if ruble_2000 > 0:
            self.__ruble_2000 = ruble_2000
        if ruble_5000 > 0:
            self.__ruble_5000 = ruble_5000
        self.__set_summa()

    def count_summa(self, second):
        if isinstance(second, Money):
            return self.summa + second.summa
        return None

    def __add__(self, other):
        if isinstance(other, Money):
            return self.summa + other.summa
        return None

    def count_difference(self, second):
        if isinstance(second, Money):
            return self.summa - second.summa
        return None

    def __sub__(self, other):
        if isinstance(other, Money):
            return self.summa - other.summa
        return None

    def count_division(self, second):
        if isinstance(second, Money):
            if second.summa != 0:
                return self.summa / second.summa
        return None

    def float_division(self, number):
        if isinstance(number, float):
            return self.summa / number
        return None

    def __truediv__(self, other):
        if isinstance(other, Money):
            if other.summa != 0:
                return self.summa / other.summa
        if isinstance(other, float):
            if other != 0:
                return self.summa / other
        return None

    def __floordiv__(self, other):
        if isinstance(other, Money):
            if other.summa != 0:
                return self.summa // other.summa
        if isinstance(other, float):
            if other != 0:
                return self.summa // other
        return None

    def float_multiplication(self, number):
        if isinstance(number, float):
            return self.summa * number
        return None

    def __mul__(self, other):
        if isinstance(other, Money):
            return self.summa * other.summa
        if isinstance(other, float):
            return self.summa * other
        return None

    def compare(self, second):
        if isinstance(second, Money):
            return self.summa > second.summa
        return None

    def __lt__(self, other):
        if isinstance(other, Money):
            if self.summa < other.summa:
                return True
            else:
                return False
        return None

    def __le__(self, other):
        if isinstance(other, Money):
            if self.summa <= other.summa:
                return True
            else:
                return False
        return None

    def __eq__(self, other):
        if isinstance(other, Money):
            if self.summa == other.summa:
                return True
            else:
                return False
        return None

    def __ne__(self, other):
        if isinstance(other, Money):
            if self.summa != other.summa:
                return True
            else:
                return False
        return None

    def __gt__(self, other):
        if isinstance(other, Money):
            if self.summa > other.summa:
                return True
            else:
                return False
        return None

    def __ge__(self, other):
        if isinstance(other, Money):
            if self.summa >= other.summa:
                return True
            else:
                return False
        return None

    def display(self):
        print(f"Количество монет с достоинством 1 копейка: {self.penny_1}")
        print(f"Количество монет с достоинством 5 копеек: {self.penny_5}")
        print(f"Количество монет с достоинством 10 копеек: {self.penny_10}")
        print(f"Количество монет с достоинством 50 копеек: {self.penny_50}")

        print(f"Количество монет с достоинством 1 рубль: {self.ruble_1}")
        print(f"Количество монет с достоинством 2 рубля: {self.ruble_2}")
        print(f"Количество монет с достоинством 5 рублей: {self.ruble_5}")
        print(f"Количество монет с достоинством 10 рублей: {self.ruble_10}")
        print(f"Количество купюр с достоинством 50 рублей: {self.ruble_50}")
        print(f"Количество купюр с достоинством 100 рублей: {self.ruble_100}")
        print(f"Количество купюр с достоинством 200 рублей: {self.ruble_200}")
        print(f"Количество купюр с достоинством 500 рублей: {self.ruble_500}")
        print(f"Количество купюр с достоинством 1000 рублей: {self.ruble_1000}")
        print(f"Количество купюр с достоинством 2000 рублей: {self.ruble_2000}")
        print(f"Количество купюр с достоинством 5000 рублей: {self.ruble_5000}")
        print(f"Общая сумма: {self.summa}")

    def read(self):
        penny_1 = int(input("Введите количество монет с достоинством 1 копейка: "))
        penny_5 = int(input("Введите количество монет с достоинством 5 копеек: "))
        penny_10 = int(input("Введите количество монет с достоинством 10 копеек: "))
        penny_50 = int(input("Введите количество монет с достоинством 50 копеек: "))

        ruble_1 = int(input("Введите количество монет с достоинством 1 рубль: "))
        ruble_2 = int(input("Введите количество монет с достоинством 2 рубля: "))
        ruble_5 = int(input("Введите количество монет с достоинством 5 рублей: "))
        ruble_10 = int(input("Введите количество монет с достоинством 10 рублей: "))
        ruble_50 = int(input("Введите количество купюр с достоинством 50 рублей: "))
        ruble_100 = int(input("Введите количество купюр с достоинством 100 рублей: "))
        ruble_200 = int(input("Введите количество купюр с достоинством 200 рублей: "))
        ruble_500 = int(input("Введите количество купюр с достоинством 500 рублей: "))
        ruble_1000 = int(input("Введите количество купюр с достоинством 1000 рублей: "))
        ruble_2000 = int(input("Введите количество купюр с достоинством 2000 рублей: "))
        ruble_5000 = int(input("Введите количество купюр с достоинством 5000 рублей: "))

        self.__penny_1 = int(penny_1)
        self.__penny_5 = int(penny_5)
        self.__penny_10 = int(penny_10)
        self.__penny_50 = int(penny_50)

        self.__ruble_1 = int(ruble_1)
        self.__ruble_2 = int(ruble_2)
        self.__ruble_5 = int(ruble_5)
        self.__ruble_10 = int(ruble_10)
        self.__ruble_50 = int(ruble_50)
        self.__ruble_100 = int(ruble_100)
        self.__ruble_200 = int(ruble_200)
        self.__ruble_500 = int(ruble_500)
        self.__ruble_1000 = int(ruble_1000)
        self.__ruble_2000 = int(ruble_2000)
        self.__ruble_5000 = int(ruble_5000)

        self.__set_summa()


if __name__ == "__main__":
    m1 = Money(
        penny_1=10,
        penny_5=5,
        penny_10=15,
        penny_50=31,
        ruble_1=24,
        ruble_2=10,
        ruble_5=5,
        ruble_10=10,
        ruble_50=2,
        ruble_100=14,
        ruble_200=10,
        ruble_500=5,
        ruble_1000=20,
        ruble_2000=2,
        ruble_5000=1
    )
    m1.display()
    print(m1.float_division(2.5))
    print(m1)
    print(m1 / 2.5)
    print(m1.float_multiplication(0.5))
    print(m1 * 0.5)
    m2 = Money()
    m2.read()
    print(m1.compare(m2))
    print(m1 > m2)
    print(m1 >= m2)
    print(m1 < m2)
    print(m1 <= m2)
    print(m1 == m2)
    print(m1 != m2)
    print(m1.count_division(m2))
    print(m1 / m2)
    print(m2.count_difference(m1))
    print(m2 - m1)
    print(m2.count_summa(m1))
    print(m2 + m1)
    m2.display()
    m2.change_amount(ruble_5=2)
    m2.display()
