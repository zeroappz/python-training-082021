# step 2
# import bank_transaction
# import bank_transaction as bt
# from bank_transaction import BankTransaction
from bank_transaction import BankTransaction as bt


def main():
    praveen = bt("Praveen", 50000)
    praveen.deposit(25000)
    praveen.withdraw(60000)
    praveen.getAccountDetails()
    print()
    sriram = bt("Sriram", 10000)
    sriram.deposit(35000)
    sriram.withdraw(20000)
    sriram.getAccountDetails()


if __name__ == "__main__":
    main()
