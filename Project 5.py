import sys

class compound_interest:

    # O(N) algo.
    # daily compount interest calculator 

    leap_year = []

    def __init__(self, year):

        # common algo. for determining which year is a leap year
        if(isinstance(year, int)): 
            if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                self.leap_year.append(True) # 366 days/year
            else:
                self.leap_year.append(False) # 365 days/year

            self.comp_interest_daily()

        else:
            print("Please type in the proper format for a year (YYYY).")

    def comp_interest_daily(self):

        amount = 0
        i = 1
        while (True):
            try:
                principal = float(input("\nPlease add the principal amount that you like to start with: $"))
                starting_amount = principal
                months_invested = 12 * int(input("How long (in years) are you planning to keep the money in the bank? "))
                extra_money = float(input("How much money are you planning to add per month: $"))

                if (extra_money != 0):
                    extra_money_time = int(input("How many months are you going to add $" + str(extra_money) + "? "))
                    if(extra_money_time > months_invested):
                        print("Invalid response. You cannot add $" + str(extra_money) + " for " 
                                + str(extra_money_time) + " months and only save for " + str(months_invested/12) + 
                                    " year(s)")
                        print("Try again...")
                        sys.exit(0)
                else:
                    extra_money_time = 0
                    
                rate = float(input("The current rate is (do not include the %): "))

                if (isinstance(principal, float) and isinstance(months_invested, int) and 
                        isinstance(extra_money, float) and isinstance(rate, float)):
                    break
            except ValueError:
                print("Please enter numbers only") 

        if(self.leap_year[0] == True): # leap year
            while (i <= months_invested): 
                if(i <= extra_money_time): # monthly deposits up till the specified number by user
                    amount = (principal + extra_money) * (1 + ((rate/100)/366)) ** (366 * (1/12))
                    principal = amount
                else: # no monthly deposits
                    amount = (principal  * (1 + ((rate/100)/366)) ** (366 * (1/12)))
                    principal = amount
                i += 1

            if(extra_money != 0):
                annual_deposit = extra_money * extra_money_time
                annual_interest = amount - annual_deposit
                interest_per_day = annual_interest/365
            else:
                annual_deposit = 0
                annual_interest = amount - starting_amount
                interest_per_month = annual_interest/12
                interest_per_day = annual_interest/365


            print("\nYour return is $" + str(round(amount, 2)) + "\n")
            print("Your monthly interest is $" + str(round(interest_per_month, 2)) + "\n")
            print("Your daily interest is $" + str(round(interest_per_day, 2)) + "\n")

        else: # not a leap year
            while (i <= months_invested): 
                if(i <= extra_money_time): # monthly deposit up till the specified number by user
                    amount = (principal + extra_money) * (1 + ((rate/100)/365)) ** (365 * (1/12))
                    principal = amount
                else: # no monthly deposits
                    amount = (principal  * (1 + ((rate/100)/365)) ** (365 * (1/12)))
                    principal = amount
                i += 1
            
            if(extra_money != 0):
                annual_deposit = extra_money * extra_money_time
                annual_interest = amount - annual_deposit
                interest_per_month = annual_interest/12
                interest_per_day = annual_interest/365
            else:
                annual_deposit = 0
                annual_interest = amount - starting_amount
                interest_per_month = annual_interest/12
                interest_per_day = annual_interest/365

            print("\nYour return is $" + str(round(amount, 2)) + "\n")
            print("Your monthly interest is $" + str(round(interest_per_month, 2)) + "\n")
            print("Your daily interest is $" + str(round(interest_per_day, 2)) + "\n")
        # banker's rounding to the nearest even number 1 * 4.5% = 1.4 instead of 1.5


obj = compound_interest(2019) # input the current year here
