class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank,
        self.company_name = company_name


class Person(Company):
    def __del__(self, first_name, last_name, salary):
        self.first_name = first_name,
        self.last_name = last_name,
        self.salary = salary

    def get_salary(self):
        if self.company_bank < self.salary:
            print("У компании не достаточно средств!")
        else:
            print(self.company_bank - self.salary)


    def personal_info(self):
        print(f"{self.first_name}, {self.last_name}")