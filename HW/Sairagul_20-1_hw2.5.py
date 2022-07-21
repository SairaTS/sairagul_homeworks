import re

class ValidCarNumber:
    def __init__(self, number):
        self.number = number


    def is_valid(self):
        is_valid = re.search(r"0([1-9]{1}KG([0-9]{3})([A-Z]{3}))", self.number)

        try:
            if self.number[is_valid.start():is_valid.end()] == self.number:
                print(f"Номер {self.number} валидный!")
        except:
            print(f"Номер {self.number} не валидный!")





number = ValidCarNumber('09KG999DAB')
number.is_valid()

