#Pritpal Singh
#CS101 MWF 12PM-12:50PM
#Created 9/8/2017
#Due 9/9/2017
import math

small_italian=int(input("How many small Italians were sold? :")) #Will ask for how many small italian sandwiches were 
large_italian=int(input("How many large Italians were sold? :")) #Will ask for how many large italian sandwiches were sold
print()
small_veg=int(input("How many small Vegetarians were sold? :")) #Will ask for how many small vegetarian sandwiches were sold
large_veg=int(input("How many large Vegetarians were sold? :")) #Will ask for how many large vegetarian sandwiches were sold
print()
small_tbird=int(input("How many small TBirds were sold?: ")) #Will ask for how many small T Bird sandwiches were sold
large_tbird=int(input("How many large TBirds were sold?: ")) #Will ask for how many large T Bird sandwiches were sold
print()

breadtotal=(float(0.5)*small_italian)+((1)*large_italian)+(float(0.5)*small_veg)+((1)*large_veg)+(float(0.5)*small_tbird)+((1)*large_tbird)
salamitotal=(float(0.3)*small_italian)+(float(0.5)*large_italian)
vegetablestotal=(float(0.2)*small_italian)+(float(0.5)*large_italian)+(float(0.5)*small_veg)+(float(1.2)*large_veg)
cheesetotal=(int(4)*small_italian)+(int(8)*large_italian)+(int(5)*small_veg)+(int(11)*large_veg)+(int(3)*small_tbird)+(int(8)*large_tbird)
turkeytotal=(float(0.4)*small_tbird)+(float(0.9)*large_tbird)
print()
print(breadtotal, "Loaves of bread")
print(salamitotal, "lbs of Salami")
print(vegetablestotal, "lbs of Veges")
print(cheesetotal, "Slices of Cheese")
print(turkeytotal, "lbs of Turkey")
print("Thanks for using the Calculator")