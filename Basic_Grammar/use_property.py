# a=12, 1.2, 4.24E10, 4.24E-10, 0o177, 0x8FF, 1+j


class Test():
    def __init__(self):
        self.number = 10

    def set_number(self, num):
        if num % 2 == 0:
            self.number = num

    def get_number(self):
        return self.number


phone = Test()
phone.set_number(11)
print(phone.number)
phone.number = 11   # this can access to 'number' method directly regardless of 'if' condtion
print(phone.number)

#==================================
class TestProperty:
    def __init__(self):
        self._number = 10

    @property  #get method
    def number(self):
        return self._number
    @number.setter # set method
    def number(self,num):
        if num%2==0:
            self._number = num


phone2 = TestProperty()
phone2.number = 11
print(phone2.number)
phone2.number = 12
print(phone2.number)
