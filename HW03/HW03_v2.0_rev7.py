###############################################################################################
#								 PRITPAL SINGH												  #
#									16235530												  #	
#									CS101													  #
#							Gradebook Software V2.0 rev7									  #	
#							  Created:  10/10/2017											  #			
#							  Modified: 10/15/2017											  #
###############################################################################################



###################################################################################################################
#								Program Features 																  #
###################################################################################################################
#This Software allows user to print grades from a gradebook file. It includes following options, 
#printing the average of the whole student in a table format, printing the highest or lowest from high to low or 
#low to high by selected category of quiz, midterm, or final, in a list format. And finally it prints the average 
#of the whole class by iteration of each student and how each student affects the final grade.


###################################################################################################################
#								function calAvgWithTable														  #
###################################################################################################################
#The software works as follows. For the average (function called calAvgWithTable), the program reads the file and 
#then in a loop it prints the student name, student quiz grade, midterm grade, and the final grade, and then the 
#program prints the average in that loop and continues in that loop for the next student until there are no more 
#students left in the grade book.


###################################################################################################################
#								function highorlow														          #
###################################################################################################################
#For the high or low (function called highorlow), the program first reads opens the file and converts the file into a 
#list. Then once the list is made, a loop is made where it takes every number in that list and converts from a string
#to an integer. After the list a variable is made to count the length of the list, which is equal to number of students.
#After this the software then has two options, to print the highest or the lowest grades. After this, the software will
#asks user how many student they want to display for the highest or the lowest. NOTE, the software will only accept a
#number that is less than or equal to the number of students in the gradebook Once this option is selected, the program 
#then asks which category they would like to sort by. It includes, Quiz, Midterm, and Final. Once the category is set. 
#Depending on the options selected, from the given inputs it will display the result.


###################################################################################################################
#								function calcClassFinalAvg														  #
###################################################################################################################
#For the final option, the software will print the class average of the final in order. Meaning that the average will be 
#printed for each number of students in order showing what the average was for the 1st student, 
#2nd student combined, and so on and so on. This is done in a loop where it keeps printing 
#until it has no more students left in the grade book.


###################################################################################################################
#								function runAgain														          #
###################################################################################################################
#the function runAgain is called to ask the user if they want to run the software again or not. it will only take input
#Yes or Y, otherwise it will exist the software.


import sys
import os
import heapq
import csv
from termcolor import colored

#Read function runAgain
def runAgain():
    global option_input
    reRunProgram = input("Would you like to continue? type 'YES' or 'Y' to continue, or press any key to exit").upper()
    if reRunProgram == "YES" or reRunProgram == "Y":
        while True:
            try:
                option_input = int(input("Enter your option try"))
            except (ValueError, TypeError):
                print("Please enter a number only")
            else:
                if 1 <= option_input <= 4:
                    option_input
                    break
                else:
                    print("Please enter number between 1 and 4")
        return
    elif reRunProgram != "YES" or reRunProgram != "Y":
        print("Goodbye. Thanks for using the UMKC Software")
        sys.exit()
        return

#Read function calAvgWithTable
def calAvgWithTable():
    while True:
        my_file = input("Please enter the name of the file: ")
        try:
            open(my_file)
            break
        except FileNotFoundError:
            print("file not found Could not find that file. please enter the file name with extension")

        except IOError :
            print("IO ERROR That file does not exist!")

	#These are the headeer lines above the table that gets printed. colored function worked in pycharm
    header_name = str(colored("Name", "red", attrs=['bold', 'underline']))
    header_quiz = str(colored("Quiz", "red", attrs=['bold', 'underline']))
    header_midterm = str(colored("Midterm", "red", attrs=['bold', 'underline']))
    header_final = str(colored("Final", "red", attrs=['bold', 'underline']))
    header_avg = str(colored("Average", "green", attrs=['bold', 'underline']))


    print("=============================================================================================================================")
    print("|", str.center(header_name,38," "),"||", str.center(header_quiz,38," "),"||", str.center(header_midterm,38," "),"||", str.center(header_final,38," " ), "||", str.center(header_avg,38," "), "|")
    print("=============================================================================================================================")
	
	#this will open the file as a reader and then read the file in csv format
    my_file = open(my_file, "r")
    reader = csv.reader(my_file)
	
	#This is the loop that prints the inside of the table along with the calculation that it needs.
    for row in reader:

        name = row[0]
        quiz = row[1]
        midterm =row[2]
        final = row[3]
        average = (int(quiz) + int(midterm) + int(final))/3
        average = format(average, ".3f")
        average = str(average)


        name = str.ljust(name, 20, " ")
        quiz = str.center(quiz, 21, " ")
        midterm = str.center(midterm, 21, " ")
        final =  str.center(final, 21, " ")
        average = str.center(average, 20, " ")
        print("| ",name, "||", quiz, "||", midterm, "||", final, "||", average, " |")
    print("=============================================================================================================================")
	#closes the file after it opens, so there is no memory leak
    my_file.close()

#read function highorlow
def highorlow():
	#the count variable is set 0 because it is used later on when it finds the legnts of the file, which is then used to determine the number of students in the gradebook
    count = 0
	#a while True, try except loop to look for the file.
    while True:
        my_file = input("Please enter the name of the file: ")
        try:
            my_file = open(my_file)
            break
        except IOError:
            print("File not found, please enter the file name again.")

	#this will open the file as a reader and then read the file in csv format into a list
    reader = csv.reader(my_file)
    my_list = list(reader)
	
	#loop that converts the numbers in that list into integers.
    for num in my_list:
        num[1] = int(num[1])
        num[2] = int(num[2])
        num[3] = int(num[3])
	
	#here the number of students in the gradebook is determined
    count = len(my_list)
	
    print("1. Print the higest grades")
    print("2. Print the lowest grades")
	
	#A loop with a try except to make sure option 1 and 2 are only selected.
    while True:
        try:
            sub_option_input = int(input("Enter your option: "))
        except (ValueError, TypeError):
            print("Please enter a number only")
        else:
            if 1 <= sub_option_input <= 2:
                break
            else:
              print("Please enter number between 1 and 2")

	#A loop where it asks user for number of scores, this is where the count comes in. if the number input is greater then the count. it will go to the print statement about how input has to be less then the number of studnets.
    while True:
        try:
            how_many_scores = int(input("How may scores you want to print?: "))
        except (ValueError, TypeError):
            print("Please enter a number only")
        else:
            if 1 <= how_many_scores <= int(count):
                break
            else:
              print("Scores must be less then or equal to the number of students in gradebook, your gradebook has",count,"Students")
	
	#A loop that will check and see what category user would like to sort from. it can only take input of quiz, midterm, and final.
    while True:
        category = input("What category would you like to choose?").upper()
        if category == "QUIZ":
            category_place = 1
            break
        elif category == "MIDTERM":
            category_place = 2
            break
        elif category == "FINAL":
            category_place = 3
            break
        else:
            print("Please enter 'Quiz', 'Midterm', or 'Final' only")


	#the heapq function will print depening what option was selected up top. high or low. 
    if sub_option_input == int(1):
        print("Showing higest grades of top", how_many_scores, "students from" , category)
        print(heapq.nlargest(how_many_scores, my_list, lambda my_list: (int(my_list[category_place]))))

    elif sub_option_input == int(2):
        print("Showing lowest grades of bottom", how_many_scores, "students from" , category)
        print(heapq.nsmallest(how_many_scores, my_list, lambda my_list: (int(my_list[category_place]))))
	#closes the file after it opens, so there is no memory leak
    my_file.close()

#read function calcClassFinalAvg
def calcClassFinalAvg():
	
	#the loop will test and see if the file is there.
    while True:
        my_file = input("Please enter the name of the file: ")
        try:
            open(my_file)
            break
        except FileNotFoundError:
            print("file not found Could not find that file. please enter the file name with extension")
            file_name = input("Please enter the name of the file: ")

        except IOError :
            print("IO ERROR That file does not exist!")
            file_name = input("Please enter the name of the file: ")
	
	#Will open the file as a read only
    my_file = open(my_file, "r")
    reader = csv.reader(my_file)
    header_title = str(colored("Calculate Final Exam Average ", "red", attrs=['bold', 'underline']))
    header_name = str(colored("Iteration Number ", "blue", attrs=['bold']))
    header_final = str(colored("Final Score Added ", "blue", attrs=['bold']))
    header_average = str(colored("Average So far ", "blue", attrs=['bold']))
    count = 0
    total = 0

	#The header of the table before the loop
    print("===========================================================================")
    print("|", str.center(header_title,88, " ", ),"|")
    print("===========================================================================")

    print("|", str.center(header_name,34," "),"||", str.center(header_final,34," "),"||", str.center(header_average,34," "), "|")
    print("===========================================================================")
	
	#the loop will then print each student's name and the final grade and the average, the average will iterate after each student.
    for row in reader:
        final = int(row[3])

        total +=final
        count +=1

        average = total/count
        average = format(average, ".3f")

        print("| ", str.center("Iteration: "+ str(count), 20, " "), "||", str.center(str(final), 21, " "), "||", str.center(str(average), 21 ," "), "|")

    print("===========================================================================")
	
	#closes the file after it opens, so there is no memory leak
    my_file.close()


#the following is the option menu. the very first print line should print the the title in red color and underlined and bold. worked on pycharm software after importing colored from termcolor
print(colored("Welcome to the UMKC software","red", attrs=['bold', 'underline']))
print("Please choose one of the following options")
option_1 = print("1. Calculate the average grade for each student.")
option_2 = print("2. Print the higest or the lowest scores based on user input")
option_3 = print("3. Find the average score of the entire class (all students) in the final exam")
option_4 = print("4. To quit")

#This loop will test for input. it can only take input of 1-4, nothing else, it uses try and error to accept a num value and a if else statement to check num value to see if it is between 1-4
while True:
    try:
        option_input = int(input("Enter your option try"))
    except (ValueError, TypeError):
        print("Please enter a number only")
    else:
        if 1 <= option_input <= 4:
            break
        else:
          print("Please enter number between 1 and 4")

#This will run the option depending on what is selected from above. after each option it will run the function it needs along with the run again fucntion to see if user wants to run the program again.
while True:
    if option_input == int(1):
        calAvgWithTable()
        runAgain()
    elif option_input == int(2):
        highorlow()
        runAgain()
    elif option_input == int(3):
        calcClassFinalAvg()
        runAgain()
    elif option_input == int(4):
        print("Goodbye. Thanks for using the UMKC Software")
        sys.exit()
