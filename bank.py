class Database:
    user_data = {'z':{
        'name':'xyz',
        'balance':00,
        'acc_no':1000,
        'acc_type': 'abc',
        'od_limit':0,
        'highest balance':0,
    }} 
    def __str__(self):
        return str(Database.user_data)
    
# d = Database()
# print(d)


from abc import ABC,abstractmethod

class requirements(ABC):
    @abstractmethod

    def deposit():
        pass
    def withdraw():
        pass
    def check_balance():
        pass

class Saving(Database,requirements):

    def sav_menu(self,user_name):
        while True:

            ui = int(input("""
            enter 1 for balance 
            enter 2 for deposit
            enter 3 for withdraw
            enter 9 to exit
            """))
            if ui == 1:
                self.check_balance(user_name)
            elif ui == 2:
                self.deposit(user_name)
            elif ui == 3:
                self.withdraw(user_name)
            else:
                print("***thankyou for using our service!***")
                break
    def deposit(self,user_name):
        amount = int(input('enter amount to deposit: '))
        self.user_data[user_name]['balance']= self.user_data[user_name]['balance']+amount
        print(f"your current balance after deposit is {self.user_data[user_name]['balance']}")
    def withdraw(self,user_name): 
        amount= int(input("enter amount to withdraw: "))
        if amount> self.user_data[user_name]['balance']:
            print("!Insufficient Balance!")
        else:
            self.user_data[user_name]['balance']=self.user_data[user_name]['balance']-amount
            print(f"collect your money")
            print(f"your current balance after withdrawl is {self.user_data[user_name]['balance']}")
    def check_balance(self,user_name):
        print(f"your current balance is Rs{self.user_data[user_name]['balance']}")
class Current_Acc(Database,requirements):
    def cur_menu(self,user_name):
        while True:
            vi=int(input("""
            enter 1 for balance
            enter 2 for deposit
            enter 3 for withdrawl
            enter 9 to exit
            """))
            if vi == 1:
                self.check_balance(user_name)
            elif vi == 2:
                self.Current_deposit(user_name)
            elif vi == 3:
                self.Current_withdraw(user_name)
            else:
                print("***thankyou for using our service!***")
                break
    def deposit(self,user_name):
        self.Current_deposit(user_name)
    def withdraw(self,user_name):
        self.Current_withdraw(user_name)
    def check_balance(self,user_name):
        print(f"your current balance after deposit is {self.user_data[user_name]['balance']}")
    def Current_deposit(self,user_name):
        amount=int(input("enter amount to deposit: "))
        self.user_data[user_name]['balance']=self.user_data[user_name]['balance']+amount
        print(f"your current balance after deposit is {self.user_data[user_name]['balance']}")
        if self.user_data[user_name]['balance']> self.user_data[user_name]['highest balance']:
            self.user_data[user_name]['highest balance']=self.user_data[user_name]['balance']
        if self.user_data[user_name]['balance']>0:
            self.user_data[user_name]['od_limit']=0.25*self.user_data[user_name]['highest balance']
    def Current_withdraw(self,user_name):
        amount= int(input("enter amount to withdraw: "))
        if amount> self.user_data[user_name]['balance'] + self.user_data[user_name]['od_limit']:
            print("!Overdraft Limit Exceeded!")
        else:
            if amount> self.user_data[user_name]['balance']:
                self.user_data[user_name]['od_limit']-= (amount - self.user_data[user_name]['balance'])
                self.user_data[user_name]['balance']-= amount
            else:
                self.user_data[user_name]['balance']=self.user_data[user_name]['balance']-amount
            print(f"collect your money")
            print(f"your current balance after withdrawl is {self.user_data[user_name]['balance']}")

class Bank(Saving,Current_Acc):
    
    __user_credentials = {'0':0}
    def __init__(self):
        print("welcome to lootea bank:deposite your money and forget for lifetime")
        self.primary_menu()
        
    def primary_menu(self):
        ui=int(input("""
        enter 1 to Login
        enter 2 to Open new account
        """))
        if ui == 1:
            self.login()
        elif ui ==2:
            self.open_acc()
    def login(self):
        un = input("enter your Username: ")
        if un  in self.__user_credentials:
            pd = int(input('enter your password: '))
            if self.__user_credentials[un]==pd:
                print("*Login successful*")
                if self.user_data[un]['acc_type']=='Saving':
                    self.sav_menu(un)
                else:
                    self.cur_menu(un)
                self.primary_menu()
        else:
            print("!Invalid user")
    def open_acc(self):
        while True:
            ac_type = int(input("""
            What type account do you want to open?
            enter 1 for Saving
                 "you will receive various benefits such as earn interest as high as 8.1%/annually
                but limited tranction monthly"
            enter 2 for Current
                "enjoy unlimited transaction and liquidity guarantee, no cost currency conversion 
                and overdraft facility"
            """))
            if ac_type == 1:
                ac_type = 'Saving'
                break
            elif ac_type == 2:
                ac_type = 'Current'
                break
            else:
                print('!Invalid Input! Please enter 1 or 2')
        name = input("enter your name->")
        adhar = int(input("enter your adhar no.->"))

        self.__user_credentials[name]=adhar

        self.user_data[name] = {'name': name,'balance':00,'acc_no': self.user_data['z']['acc_no']+1,'acc_type':ac_type,'od_limit':00,'highest balance':00} 

        print("your name is your username and adhar is your password") 

        self.primary_menu()   


c1=Bank()
    


        