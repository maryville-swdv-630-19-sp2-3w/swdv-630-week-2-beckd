import datetime #to evaluate the user's birthdate and print out their current age
class CheckingAccount:
    def __init__(self, name, surname, birthdate, address, telephone, accountNumber, email="none"):
        self.name = name 
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.accountNumber = accountNumber
        self.__balance = 0 #the balance is set to a private method, so it can't be accessed externally 
        
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age
    
    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+')'
    
    def debit(self, amount): #method to debit a user's balance
        self.__balance -= amount #accesses the balance and decrements it
        print("You've taken $%d out of your account. Your current balance is $%d"%(amount, self.__balance)) 
        print()
        print("Your transaction has been completed, thank you for choosing DaveCo Savings and Loan!")
        print()
        return self.__balance
    
    def credit(self, amount):
        self.__balance += amount #accesses the balance and increments it
        print("You've deposited $%d into your account. Your current balance is $%d"%(amount, self.__balance))
        print()
        print("Your transaction has been completed, thank you for choosing DaveCo Savings and Loan!")
        print()
        return self.__balance
    
def main():
    customer = CheckingAccount( #creates instance of CheckingAccount object with these values
        "Dave",
        "Beck",
        datetime.date(1982, 4, 12),
        "123 Main St.",
        "555-123-4567",
        "12345",
        "dave@fakeemail.com")
    print(customer.name) #printout of all attributes
    print(customer.surname)
    print(customer.age())
    print(customer.address)
    print(customer.telephone)
    print(customer.accountNumber)
    print(customer.email)
    print()
    print()
    while True: #my take on what you meant by 'driver application'
        print("Welcome to DaveCo Savings and Loan.") #welcome message in shell
        action = "deposit" #action defaulted to making a deposit
        actionType = input("Would you like to make a deposit or withdrawl (please enter d or w)?: ") #gets the user input on what action the want to perform
        validInputs = ["d", "w", "D", "W"] #array of all acceptable inputs
        while actionType not in validInputs: #indefinite loop to make user a valid input was taken for actionType
            print("You must enter either a 'd' or a 'w' to proceed") #error message if True
            actionType = input("Would you like to make a deposit or withdrawl (please enter d or w)?: ") #gets another input
        if actionType == "d" or actionType == "D": #if statement to get either 'deposit' or 'withdraw' for printing purposes
            action = "desposit"
        else:
            action = "withdraw"
        amount = int(input("Please enter the amount to %s: "%(action))) #gets the amount to either deposit or withdraw
        while amount < 0: #check to make sure number is greater than 0, loops until it is
            print("You must enter a positive number to proceed")
            amount = int(input("Please enter the amount to %s: "%(action)))
        if actionType == "d": #directs them toward either the credit or debit function within the class
            customer.credit(amount)
        else:
            customer.debit(amount)
        #once a transaction is completed, it'll start over
    
main()