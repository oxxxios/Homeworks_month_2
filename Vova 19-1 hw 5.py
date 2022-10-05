import re

class ValidCarNumber:
    def __init__(self, number):
        self.number = number

    def is_valid(self):
        self.is_valid = re.search(r"([0-9]{2})([A-Z]{2})([0-9]{3})([A-Z]{3})",self.number)

        if self.is_valid:
            print("car number is valid!")
        else:
            print("car number is invalid!")

valid = ValidCarNumber(input("transport number:"))
valid.is_valid()