class Fraction:
    def __init__(self, num, dem):
        if not isinstance(num, int) or not isinstance(dem, int):
            raise TypeError
        elif dem == 0:
            raise ZeroDivisionError

        nwd = self.gcd(num, dem)
        if dem < 0:
            self.num = -num//nwd
            self.dem = -dem//nwd
        else:
            self.num = num//nwd
            self.dem = dem//nwd

    def getNum(self):
        return self.num

    def getDem(self):
        return self.dem

    def gcd(self, a, b):
        # Greatest common denominator
        a, b = abs(a), abs(b)
        if a == b:
            return a
        if a < b:
            a, b = b, a
        while b:
            a, b = b, a%b
        return a

    def hcm(self, a, b):
        # Highest common multiple
        a, b = abs(a), abs(b)
        if a == b:
            return a
        return a*b // self.gcd(a, b)

    def __str__(self):
        nwd = self.gcd(self.num, self.dem)
        return "%d/%d" % (self.num//nwd, self.dem//nwd)

    def __add__(self, fract):
        dem = self.hcm(self.dem, fract.dem)
        num = dem*self.num//self.dem + dem*fract.num//fract.dem
        return Fraction(num, dem)

    def __sub__(self, fract):
        dem = self.hcm(self.dem, fract.dem)
        num = dem*self.num//self.dem - dem*fract.num//fract.dem
        return Fraction(num, dem)

    def __mul__(self, fract):
        return Fraction(self.num*fract.num, self.dem*fract.dem)

    def __truediv__(self, fract):
        return Fraction(self.num*fract.dem, self.dem*fract.num)

    def __eq__(self, fract):
        if (self-fract).num == 0:
            return True
        return False

    def __gt__(self, fract):
        if (self - fract).num > 0:
            return True
        else:
            return False

    def __ge__(self, fract):
        return self.__eq__(fract) or self.__gt__(fract)

    def __lt__(self, fract):
        if self.__eq__(fract):
            return False
        else:
            return not self.__gt__(fract)

    def __le__(self, fract):
        return self.__eq__(fract) or self.__lt__(fract)
