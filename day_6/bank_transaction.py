class BankTransaction(object):
    default_acc = 30900305
    bankName = "SBI"

    def __init__(self, name, balance=0):
        ''' setting up the user bank account '''
        self.name = name
        self.balance = balance
        self.account_no = BankTransaction.default_acc
        BankTransaction.default_acc += 1

    def deposit(self, depositAmount):
        print("I am gonna deposit sum amount of Rs. {} to {}".
              format(depositAmount, self.account_no))
        self.balance += depositAmount

    def withdraw(self, withdrawlAmount):
        print("I am gonna withdraw sum amount of Rs. {} to {}".
              format(withdrawlAmount, self.account_no))

        if (self.balance < withdrawlAmount):
            print("You account has insufficient fund...")
        else:
            self.balance -= withdrawlAmount

    def getAccountDetails(self):
        print("My {} account number {} and balance amount Rs. {}".
              format(BankTransaction.bankName, self.account_no, self.balance))


'''
I am gonna deposit sum amount of Rs. 25000 to 30900305
My SBI account number 30900305 and balance amount Rs. 75000

I am gonna deposit sum amount of Rs. 35000 to 30900306
My SBI account number 30900306 and balance amount Rs. 45000
'''
