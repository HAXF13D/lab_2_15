class Money:

    def __init__(self, ruble, penny):
        self.__size = 100
        self.__value = [0 for _ in range(100)]
        self.__length = 0
        self.set_ruble(ruble)
        self.set_penny(penny)

    @property
    def size(self):
        return self.__size

    @property
    def value(self):
        return self.__value

    def set_ruble(self, value):
        if isinstance(value, int):
            temp = [0 for _ in range(98)]
            self.__value[2:100] = temp
            rubles = int(value)
            i = 2
            while rubles > 0:
                self.__value[i] = rubles % 10
                rubles = rubles // 10
                i += 1
            self.__length = i

    def set_penny(self, value):
        if isinstance(value, int):
            temp = [0 for _ in range(2)]
            self.__value[0:2] = temp
            penny = int(value)
            i = 0
            penny = penny % 100
            while penny > 0:
                self.__value[i] = penny % 10
                penny = penny // 10
                i += 1

    def __str__(self):
        temp = ""
        marker = False
        for i in reversed(self.__value):
            if 0 <= i <= 9:
                if 1 <= i <= 9:
                    marker = True
                if marker:
                    temp = temp + str(i)
        penny = temp[-2:]
        ruble = temp[0:len(temp) - 2]
        return f"{ruble}.{penny}"

    def __len__(self):
        return self.__length

    def __compare(self, second):
        if self.__length > len(second):
            return 1
        if self.__length < len(second):
            return 2
        if self.__length == len(second):
            for i in range(len(second) - 1, -1, -1):
                if self.value[i] > second.value[i]:
                    return 1
                if self.value[i] < second.value[i]:
                    return 2
        return 3

    def __lt__(self, other):
        if isinstance(other, Money):
            info = self.__compare(other)
            if info == 1:
                return True
            else:
                return False
        raise ValueError

    def __le__(self, other):
        if isinstance(other, Money):
            info = self.__compare(other)
            if info == 1 or info == 3:
                return True
            else:
                return False
        raise ValueError

    def __eq__(self, other):
        if isinstance(other, Money):
            info = self.__compare(other)
            if info == 3:
                return True
            else:
                return False
        raise ValueError

    def __ne__(self, other):
        if isinstance(other, Money):
            info = self.__compare(other)
            if info == 3:
                return False
            else:
                return True
        raise ValueError

    def __gt__(self, other):
        if isinstance(other, Money):
            info = self.__compare(other)
            if info == 2:
                return True
            else:
                return False
        raise ValueError

    def __ge__(self, other):
        if isinstance(other, Money):
            info = self.__compare(other)
            if info == 2 or info == 3:
                return True
            else:
                return False
        raise ValueError

    def __add__(self, other):
        if isinstance(other, Money):
            info = []
            ost = 0
            for i in range(100):
                ost = self.value[i] + other.value[i] + ost
                info.append(ost % 10)
                ost = ost // 10
            temp = ""
            marker = False
            for i in reversed(info):
                if 0 <= i <= 9:
                    if 1 <= i <= 9:
                        marker = True
                    if marker:
                        temp = temp + str(i)
            penny = temp[-2:]
            ruble = temp[0:len(temp) - 2]
            return f"{ruble}.{penny}"

    def __sub__(self, other):
        if isinstance(other, Money):
            info = []

            d1 = self.value.copy()
            d2 = other.value.copy()

            result = self.__compare(other)

            if result == 1:
                sign = 1
            if result == 2:
                sign = -1
            if result == 3:
                return 0

            if sign == 1:
                for i in range(100):
                    if d1[i] >= d2[i]:
                        info.append(d1[i] - d2[i])
                    else:
                        info.append(10 + d1[i] - d2[i])
                        if i != 99:
                            d1[i + 1] -= 1
            else:
                for i in range(100):
                    if d2[i] >= d1[i]:
                        info.append(d2[i] - d1[i])
                    else:
                        info.append(10 + d2[i] - d1[i])
                        if i != 99:
                            d2[i + 1] -= 1
            temp = ""
            marker = False
            for i in reversed(info):
                if 0 <= i <= 9:
                    if 1 <= i <= 9:
                        marker = True
                    if marker:
                        temp = temp + str(i)
            penny = temp[-2:]
            ruble = temp[0:len(temp) - 2]
            if sign == 1:
                return f"{ruble}.{penny}"
            if sign == -1:
                return f"-{ruble}.{penny}"


if __name__ == '__main__':
    m1 = Money(100, 20)
    m1.set_ruble(200)
    m1.set_penny(54)
    m2 = Money(400, 52)
    print(m1 > m2)
    print(m1 >= m2)
    print(m1 == m2)
    print(m1 != m2)
    print(m1 <= m2)
    print(m1 < m2)
    print(m1 - m2)
    print(m2 + m1)
