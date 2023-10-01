class OverdraftError(Exception):
   def __init__(self,message="Insufficient Funds"):
            self.message = message

class BankAccount:
    #Class Attribute
    __routingNumber = "268974"
    __branchAddress = "55 Main Street"
    __branchPhone = "555-1212"
    @classmethod
    def getRoutingNumber(cls):
        return cls.__routingNumber
    #Constructor
    def __init__(self,accountNum,initialDeposit):
        self.__accountNumber = accountNum
        self.__balance = float(initialDeposit)
    # Destructor method
    def __del__(self):
        if self.__balance > 0:
            print("Issuing Check for $",self.__balance)
    # User Friendly printing
    def __str__(self):
        return "Account: "+self.__accountNumber+" Balance: "+str(self.__balance)
    # Mutator Method
    def deposit(self,amount):
        if amount < 0:
            raise ValueError("Deposits must be greater than zero")
        self.__balance += amount
    def withdraw(self,amount):
        if amount < 0:
            raise ValueError("Withdrawals must be greater than zero")
        if amount > self.__balance:
            raise OverdraftError("Overdraft!!!")
        self.__balance -= amount
    # Accessor method
    def getBalance(self):
        return self.__balance

#Main Program Starts Here
myAccount = BankAccount("1234",0)

while True:
    choice = int(input("Welcome to Bank!!\n\t1: Check Balance\n\t2: Deposit\n\t3: Withdraw\n\t4: Exit\nEnter Choice:"))
    if choice==1:
        print("Balance = $",myAccount.getBalance())
    elif choice == 2:
        value = float(input("Enter amount to deposit: "))
        myAccount.deposit(value)
    elif choice == 3:
        value = float(input("Enter amount to withdraw: "))
        myAccount.withdraw(value)
    elif choice == 4:
        break

print("Thank you for banking at Bank!!!")
print(myAccount)



