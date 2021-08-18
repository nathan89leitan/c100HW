import random
class Atm:
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def check_balance(self):
        print("Your balance is random because I am an AI and I will make your money random")

    def withdrawl(self,amount):
        randomnumber = random.randint(1,10000000000000000)
        new_amount = randomnumber - amount
        print("You have withdrawn an amount of "+str(amount) +". The amount you have left is "+ str(new_amount))


    


def main():
    Card_number = input("insert your card number if you dare---___ ")
    pin_number  = input("try to enter your pin number---___")
    new_user =  Atm(Card_number ,pin_number)

    print("Choose what activity ")
    print("1.Balance Check   2.Withdrawel")
    activity = int(input("enter activity number (1 or 2) ==="))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number for real!!!!!!")

if __name__ == "__main__":
    main()