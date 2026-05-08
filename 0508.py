import pandas

expenseList = {}


class Expense:
    def __init__(self, expenseAmount, item):
        self.expenseAmount = expenseAmount
        self.item = item

    def insertExpense(self):
        global expenseList
        if self.item in expenseList:
            expenseList[self.item] += self.expenseAmount
        else:
            expenseList[self.item] = self.expenseAmount


checkList = False

while checkList == False:
    expense = input("Enter expense amount: ")
    if expense == "check":
        checkList = True
        for row in expenseList:
            print(f"{row} | {expenseList[row]}")
    else:
        item = input("Enter item: ")
        inf = Expense(int(expense), item)
        inf.insertExpense()
