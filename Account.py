class Account(object):

    def __init__(self, accountId: int, balance: int):

        self.accountId = accountId
        self.balance = balance

    def deposit(self,balance,amount: int):

        amount = input("Enter deposit amount")

        if amount >= 999999999:

            raise ValueError("""Amount too high..\n
            Enter amount :""")
        
        else:
             
             deposit = amount
             balance = balance + deposit
        return balance
                      

    def withdraw(self,balance,amount: int):



        if balance == 0:

            raise Exception("Balance is 0..")

        else:                
                # withdraw balance = balance - amountWithdrawn

                withdraw = balance - amount
                
                balance = withdraw

                return balance


    def getBalance(self,balance):

        return balance


