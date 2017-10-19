#Real Estate Calculator
#Created 9/27/2017
#Version 2.1 r19
#CS 101
#© Pritpal Singh


#Program Info Below:
#In this program, the calculator for real estate will calculate your monthly 
#payments and the total interest for the house price. The program starts out 
#by asking the price of the house. The program will only accept a positive 
#number for the price of the house. Once the house price is an accepted. 
#The program will then prompt user for input of down payment. The down 
#payment can be Yes or No. if the down payment is no. then down payment 
#will become 0 by default. But if it is yes, the program will prompt for the 
#amount. The prompt will only accept an amount that is less than the house 
#price and if it is a number, otherwise it will keep prompting for a number. 
#After down payment the user will enter be prompted for credit score will 
#the interest rate will be determined. Once your interest rate is determined. 
#The program will run two formulas where it will calculate the monthly 
#payment and total interest. After it calculates it displays the price from 
#beginning of 10 years to 25 years, by increasing by 1 year. After it prints.
#It will ask if you want to run the program again.


while True:
	#These value are being reset because once the program is restarted the values are going to default to zero and the user will input them again.
    houseprice = 0
    downpayment = 0
    interest_rate =0

    #in the beginning of the code, the program prompts for input for house price by asking what the price of the house is
    houseprice = input("Enter the price of your dream house: ")

    #This loop will check and see what the user has put in for the houseprice input. if the user has put in a character
    #that is not a number and it will loop and tell them that the input of the house must be a positive number only. the loop will
    #keep going until a positive number is entered, where it will stop the loop.
    while houseprice.isdigit()== False:
        print("House price must be a positive number only")
        houseprice = input("Enter the price of your dream house")

    #The houseprice will now become a integer after it exists the loop so it can be used later on in the code in a function
    houseprice=int(houseprice)

    #this downpayment input will ask if the user is going to make any downpayments
    downpayment=input("Are you making any down payments?").upper()

    #This loop is for the downpayment. in this loop the program first detects for Yes, Y, No, N. if the input is Yes, the user is prompted for input again for the amount of the input.
    #after the prompt is program then goes into another loop where it checks and see if the input is digit or alpha. if the input is alpha the program loops untill a positive number is entered.
    #if the input is digit the program then loops and see if the input, downpayment is greater then or equal to, or less then the price of the house.
    #if it is greater then or equle too, the program loops and asks for a input that is less then the house price.
    #if the downpayment is less then the house price, the downpayment variable gets reassigned to it self as a integer downpayment and it breaks or exists the loop.
    while True:
        if downpayment == "YES" or downpayment == "Y":
            downpayment=input("How much is your down payment")
            while True:
                while downpayment.isdigit() == False:
                    print("Please Enter a positive number only")
                    downpayment=input("How much is your down payment")
                    continue

                while downpayment.isdigit() == True:
                    downpayment = int(downpayment)

                    if downpayment >=  houseprice:
                        print("Down payment has to be less then house price")
                        downpayment=input("How much is your down payment")
                        while  downpayment.isalpha():
                            print("Please enter a Positive number only.")
                            downpayment=input("How much is your down payment")
                    elif downpayment < houseprice:
                        downpayment = int(downpayment)
                        break

                break
            break

        elif downpayment == "NO" or downpayment == "N":
            downpayment = int(0)
            break
        else:
            print("Please Enter Yes or No only")
            downpayment=input("Are you making any down payments").upper()

    #down is set to integer for future calculations
    downpayment = int(downpayment)

    #interest rate is
    interest_rate = 0

    #credit score is a imput prompt. it will ask the user what their credit score.
    creditscore = input("Please enter your credit score")

    #in this loop. the loop tests the for the input of the credit score.
    #if the input contains any alpha the program will keep looping untill the credit score input is a number.
    #after a number is entered the program then does the loop where it does comparision.
    #if the credit score is between 0 and 500 the interest rate becomes 0.05 or 5 percent.
    #if the credit score is between 501 and 700 the interest rate becomes 0.02 or 2 percent.
    #if the interest rate is anything else like greater then it becomes 0.01 or 1 percent.
    while True:
        while creditscore.isalpha() == True:
            print("Please enter your credit score in number format only")
            creditscore = input("Please enter your credit score")

        while creditscore.isdigit() == True:
            creditscore= int(creditscore)
            if creditscore >= 0 and creditscore <= 500:
                interest_rate = float(0.05)
            elif creditscore >= 501 and creditscore <= 700:
                interest_rate = float(0.02)
            else:
                interest_rate = float(0.01)
            break
        break

    #Prints a extra blank line
    print("")

    #print tells you what your interest rate is after you type in your credit score
    print("Based on your Credit Score, your total interest rate is", interest_rate)
	
	#Prints a extra blank line
	print("")
	
    #min_years is the first year you wish to start your calculations. if you wish to start at a later or earlier year. change this variable
    min_years = 10

    #this def called calMonthlyPayments is a function that will calculate the monthly payment by
    #using the formula.
    def calMonthlyPayments (min_year):
        payment_per_month =((houseprice - downpayment) * ((1 + interest_rate) ** min_years)) / (12 * min_years)
        #payment_per_month = round(payment_per_month, 2)
        return payment_per_month
        #

    #this def called calTotalInterest is a function that will calculate the total interest by using the formula.
    #this function also calls a variable from the previous function to complete the formula
    def calTotalInterest(min_year):
        payment_per_month = calMonthlyPayments(min_year)
        total_interest = (payment_per_month * min_years * 12) - (houseprice - downpayment)
        #total_interest = round(total_interest, 2)
        return total_interest
        #Total interest = (A * n * 12) – (P – D)


    #this loop will now print the total payments and total interest based on the formula from above.
    #in this loop starthing is 10 because the first year has to be 10.
    #and it will increment and will go all the way up to 25 years and then break.
	#26 is when the loop will stop. since it is less then 26 the program will stop at 25 years. if you wish to increase and go out further, change the number after min years < to the year you want +1.
	#IE if you wanted to stop at 59 years. you would make min years < 60.
    while min_years < 26:
        print("Pay in", min_years,"Years.", "Monthly payment is $",round(calMonthlyPayments(min_years), 2), "and total interest is $",round(calTotalInterest(min_years), 2))
        min_years +=1

	#Run again means that if the user would like to run the calculator again. if they type yes it will loop back up to the top and start over
	#if they type anything else the program will exit.
    run_again = input("Would you like to use the calculator again? if so type Yes, if not press any key to exit").upper()
    if run_again == "YES":
        continue
    else:
        print("Thanks for using the program, have a great day")
        break
