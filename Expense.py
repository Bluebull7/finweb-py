from datetime import date as Date
import TransactionCategory

class Expense(object):


    def __init__(self, expenseId: int, date: Date, amount: float, category: TransactionCategory):
        self.expenseId = expenseId
        self.date = date
        self.amount = amount
        self.category = category

    def getExpenseDetails(self,expenseId,date,amount,category):
        
        return expenseId, date, amount, category


    
