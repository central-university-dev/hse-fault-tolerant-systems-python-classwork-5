# Python program showing a use
# of get() and set() method in
# normal function
class Human:
    def __init__(self, age=0):
        self._age = age

    # getter method
    def get_age(self):
        return self._age

    # setter method
    def set_age(self, x):
        self._age = x


me = Human()

# setting the age using setter
me.set_age(18)

# retrieving age using getter
print(me.get_age())
print(me._age)


# Python program showing the use of
# @property
class Human:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


mark = Human()
mark.age = 19
print(mark.age)
