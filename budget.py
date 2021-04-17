class Budget:

    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def deposit(self):
        deposit_amount = float(input('Enter amount to deposit: \n'))
        self.balance += deposit_amount
        print(f'Your new balance is #{self.balance}')
        return exist()

    def withdrawal(self):
        withdraw_amount = float(input('Enter amount to withdraw: '))
        if withdraw_amount > self.balance:
            print('Insufficient cash balance')
        else:
            self.balance -= withdraw_amount
            print(f'Collect your cash, your new balance is ₦{self.balance}')
            return exist()

    def transfer(self, transfer_money):
        print(f'Transfer from {self.category} budget')
        transfer_amount = float(input('Enter amount to transfer: '))
        if transfer_amount >= self.balance:
            print('Insufficient cash balance')
            exist()
        else:
            self.balance -= transfer_amount
            print(f'Transfer Successful: Your new {self.category} balance is ₦{self.balance}')
            exist()

    def get_balance(self):
        print(f"{self.category} balance: ₦{self.balance}")
        exist()


def food():
    print('FOOD')
    food1 = Budget('food', 800)
    food_Option = input('''Your options
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance
        Input here: ''')
    if food_Option == '1':

        food1.deposit()
    elif food_Option == '2':
        food1.withdrawal()
    elif food_Option == '3':
        transfer = input('''which category would you like to transfer to?
            1.Clothing
            2.Entertainment
            Input here: ''')
        if transfer == '1':
            food1.transfer('Clothing')
        elif transfer == '2':
            food1.transfer('Entertainment')
        else:
            print('invalid option')
    elif food_Option == '4':
        food1.get_balance()
    else:
        print('invalid option selected')
        welcome()


def clothing():
    print('CLOTHING')
    clothing1 = Budget('clothing', 5000)
    clothing_Option = input('''Your options
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance 
        Input here: ''')
    if clothing_Option == '1':
        clothing1.deposit()
    elif clothing_Option == '2':
        clothing1.withdrawal()
    elif clothing_Option == '3':
        category_transfer = input('''which category would you like to transfer to?
            1.food
            2.Entertainment
            Input here: ''')
        if category_transfer == '1':
            clothing1.transfer('food')
        elif category_transfer == '2':
            clothing1.transfer('Entertainment')
        else:
            print('invalid option')
    elif clothing_Option == '4':
        clothing1.get_balance()
    else:
        print('invalid option selected')
        welcome()


def entertainment():
    print('ENTERTAINMENT-BUDGET')
    Entertainment = Budget('Entertainment', 2000)
    Entertainment_Option = input('''You've the following options
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Theck balance 
        Input here: ''')
    if Entertainment_Option == '1':
        Entertainment.deposit()
    elif Entertainment_Option == '2':
        Entertainment.withdrawal()
    elif Entertainment_Option == '3':
        transfer_to = input('''which category would you like to transfer to?
            1.food
            2.clothing
            Input here: ''')
        if transfer_to == '1':
            Entertainment.transfer('food')
        elif transfer_to == '2':
            Entertainment.transfer('clothing')
        else:
            print('invalid option')
    elif Entertainment_Option == '4':
        Entertainment.get_balance()
    else:
        print('invalid option selected')
        welcome()


def welcome():
    try:
        print('== WELCOME TO THE BUDGET APP ==')
        select_option = int(input('''What would you like to budget for?
    1. Food 
    2. Clothing 
    3. Entertainment 
    4. Exit
    Input here: '''))
        
        if select_option == 1:
            food()
        elif select_option == 2:
            clothing()
        elif select_option == 3:
            entertainment()
        elif select_option == 4:
            print("Good bye!")
        else:        

            print('Invalid Option, Try again')
            exist()
    except ValueError:
        print("Please input a valid digit")
        return welcome()


def exist():
    try:
        exist_now = int(input("""Do you want to perform another transaction? \n
    1. Yes
    2. No

    Input Here:
    """))
        if exist_now == 1:
            welcome()
        elif exist_now == 2:
            print('Thank you for using the budget app')
        else:
            print('Invalid Input, Please try again')
            welcome()
    except ValueError:
        print('input Number')
        return exist()


welcome()
