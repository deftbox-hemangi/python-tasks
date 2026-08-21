class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses= set()

    def add_income(self, income):
        self.incomes.add(income)

    def add_expense(self, expense):
        self.expenses.add(expense)

    def account_info(self):
        print("Name:", self.firstname, self.lastname)


p=PersonAccount("John", "Doe")
p.add_income(100)
p.add_expense(200)
print(p.incomes)
print(p.expenses)
p.account_info()