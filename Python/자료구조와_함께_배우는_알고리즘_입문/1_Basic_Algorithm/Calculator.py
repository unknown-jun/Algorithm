class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

a = FourCal(4,2)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal(4,2)
print(b.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result
    
c = SafeFourCal(12452, 0)
print(c.div())