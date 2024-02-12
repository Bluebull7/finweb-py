import TransactionCategory

class Transaction(object):

    def __init__(self, transactionId: int, amount: float, category: TransactionCategory):

        self.transactionId = transactionId
        self.amount = amount
        self.category = category


    def getTransactionDetails(self) -> str:

        return("A transaction of type: " + str(self.category) + "\n Amount : " + str(self.amount))
    
    

