class ExpenseTracker:
    def __init__(self,date,description,transaction_type,amount):
        self.date = date
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount

m = ExpenseTracker("12jan","dinner with friends","Credit",2000)
print(m.amount)
        