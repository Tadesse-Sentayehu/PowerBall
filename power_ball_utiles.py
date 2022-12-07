
import random

# in this white_ball class we add 5 num with None value and we use two method
# first one is Winner second one is lucky and with the help random.randit the number
# will be random number and the numbers from (1,20)

class White_ball:
    def __init__(self,num1=None, num2=None, num3=None, num4=None, num5=None):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5

    def getnum1(self):
        return self.num1

    def getnum2(self):
        return self.num2

    def getnum3(self):
        return self.num3

    def getnum4(self):
        return self.num4

    def getnum5(self):
        return self.num5

    def winner(self):
        winner1 = random.randint(1, 20)
        winner2 = random.randint(1, 20)
        winner3 = random.randint(1, 20)
        winner4 = random.randint(1, 20)
        winner5 = random.randint(1, 20)
        self.num1 = winner1
        self.num2 = winner2
        self.num3 = winner3
        self.num4 = winner4
        self.num5 = winner5
        return winner1, winner2, winner3, winner4, winner5

    def lucky(self):
        lucky1 = random.randint(1, 20)
        lucky2 = random.randint(1, 20)
        lucky3 = random.randint(1, 20)
        lucky4 = random.randint(1, 20)
        lucky5 = random.randint(1, 20)
        self.num1 = lucky1
        self.num2 = lucky2
        self.num3 = lucky3
        self.num4 = lucky4
        self.num5 = lucky5
        return lucky1, lucky2, lucky3, lucky4, lucky5

# in this power_ball class we have unique_numer with value and we use the 2 method
# first one is big ball  second one is big_ball2 and with the help random.randit the number
# will be random number and the numbers from (1,10) and they are our special power_balls


class Power_ball:
    def __init__(self,unique_number=None):
        self.unique_number = unique_number

    def getunique1(self):
        return self.unique_number

    def big_ball1(self):
        strong_number = random.randint(1,10)
        self.unique_number = strong_number
        return strong_number

    def big_ball2(self):
        strong_number2 = random.randint(1, 10)
        self.unique_number = strong_number2
        return strong_number2


