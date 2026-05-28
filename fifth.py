# if else conditional statements

# if(7>8):
#     print('ohho')
#     print(8+9)
# else :
#     print('woow')

# name=input('enter your name ')
# if(name=='rohit'):
#     print('trainer at madrid')

# else:
#         print('student at madrid')

# algorhitims
# step by step procedures to perform a specific task

# create a variable with input function with type conversion(int)
# use if else, for getting the user input and checking the condition
# if age is greater than or equal to 18 the user is eligible to vote
# if condition is true, print youre eligible
# if  age is less than 18 the user is not eligible to vote, else condition is used
#  if condition is false else 

# pseudo code
# create a variable with input fn age use type conversion---->(int)
#  create a if else stement, if age>=18--->print(user can vote)
#  else statment, if age<18 else statment print----->(user cannot vote)

# age=int(input())


# 1 working age group
# create a currentyear(2026)
# create a Birthyear variable with input fn--->type conversion--->(int)
# use if else statment
# if year----->






# currentYear= 2026
# birthyear= int(input('enter your age '))
# currentAge= currentYear-birthyear
# if(currentAge>=18 and currentAge<=61):
#     print('working age group')
# else:
#     print('non working age group')

    ## Problem 2: Shopping Bill with Discount

# Take the price and quantity of an item as input from the user.
#  Convert them to appropriate numeric types and calculate the total amount.
#   If the total amount is greater than 1000 
#  *and* quantity is more than 5, apply a 10% discount. 
#  Otherwise, print the normal total Display final payable amount.

# price=int(input('enter the price: '))
# quantity=int(input('enter the quantity: '))
# totalAmmount= price*quantity
# if(totalAmmount>=1000 and quantity>=5):
#     print('10 percent disc availed at checkout')
# else:
#     print('normal price')



# student percentage
# maths=int(input('enter maths marks '))
# science=int(input('enter science marks '))
# Sst=int(input('enter sst marks '))
# obtaniedMarks= maths+science+Sst
# percentage= obtaniedMarks/300*100

# if(percentage>40 and maths>=33 and science>=33 and Sst>=33):
#     print('pass')
#     print('your percentage ',percentage)
# else:
#     print('fail')
#     print('your percentage',percentage)
 

# problem 5

# weight=float(input('enter your weight '))
# height=float(input('enter your height '))
# bmi=weight/height*height

# if(bmi<18.5 and bmi<=24.9):
#     print('normal')

# elif(bmi>=25):
#     print('overweight')
# else:
#     print('underweight')



# loan eligibility crietera

# monthlyInc=int(input('enter your monthly Income '))
# age=int(input('enter your age '))

# if(monthlyInc>=25000 and age>=21 and age<=60):
#     print('youre eligible for loan')
# else:
#     print('youre not eligible for loan')




## Problem 8: Electricity Bill Calculator

# Ask the user to enter the number of units consumed as a string and 
# convert it into an integer. Calculate total bill:
# * First 100 units → 5 per unit
# * Next 100 units → 7 per unit
# * Remaining units → 10 per unit
#   After calculating the bill, if the total bill is more than 1500 *or*
#  units are more than 250, add a surcharge of 5%.
# Print total units, bill amount,
#  and final amount after surcharge if applicable.


# unitElec=int(input('enter units consumed '))
# bill=unitElec*5            #for 100 unit consumption
# bill2=unitElec*7          #for 100+ unit consumption
# bill3=unitElec*10         #for 200+ unit consumption
# surBill=bill3*5/100
# total=surBill+bill3+bill2+bill



# if(unitElec<=100 ):
#     print('your bill ',bill)

# elif(unitElec>=100 and unitElec<=200):
#     print('your bill ',bill+bill2)

# elif(unitElec>=200 and unitElec<=249):
#     print('total bill ',bill1+bill2+bill3)

# elif(unitElec>=250):
#     print('your bill', total)

# else:
#     print('base bill')



# #2nd try
# Units=float(input('enter units consumed '))
# totalBill=0

# if(units<=100):
#     totalBill=units*5
#     if(totalBill>=1500)
#     surcharge=5/100*totalBill
#     grandtotal=totalBill+surcharge
#     print('your bill ',grandtotal)
# else:
#     print('your bill ',totalBill)
# elif(unit>100 and unit<=200):







### Problem 9: Salary Hike and Tax Check

#Ask the user to enter their current salary (float) and performance rating (out of 5).
#  If rating is greater than or equal to 4 and salary is less than 80000,
#  increase salary by 15% otherwise increase by 5%.
#   Then check using comparison and logical operators whether the
#  new salary is taxable (greater than 50000).
#   Print old salary, new salary, and taxability status


#points to note for this problem
#salary to be increased by 15 % if rating is 4 out of 5 and salary is less than 80k
# salary above 50k is taxable

# baseSal=float(input('enter your salary '))
# rate=float(input('enter your rating '))
# tax=baseSal*6/100


# if(baseSal<80000.00 and rate>=4.00):
#     hike=15/100*baseSal
#     newSal=hike+baseSal
#     print('your salary inc taxes: ',newSal)
#     print('taxes charged: ',tax)
#     print('total salary: ',newSal-tax)
# else:
#     print('your salary, no hike received: ',baseSal-tax)

# if(baseSal<80000.00 and rate>=4.00):
#     hike2=5/100*baseSal
#     newSal2=hike2+baseSal
#     print('your salary inc taxes: ',newSal2)
#     print('taxes charged: ',tax)
#     print('total salary ',newSal2-tax)

# salary= float(input('enter your salary '))
# rating= int(input('enter your rating '))
# hike=0
# totalSal=0


# if(salary<80000.00 and rating>=4):
#     print('your salary ',s)
# elif(salary>=80000.00 and rating>=4):
#     print('your salary: ',totalSal2)
# (totalSal>=50000 and totalSal2>=50000 and salary>=50000):
#         print('your salary is taxable')
# else:
#     print('your base salary: ',salary)



# # Take age and city name as input. Convert age to integer. Using logical operators,
#  verify that the person is at least 18 and does not live in a restricted city 
#  named "TestCity". Print whether they can vote in the local booth. 
#  Also print how many years are left if they are
#   underage (use arithmetic operator).


# age=int(input('enter your age '))
# city=input('your city ')
# testCity='jaipur'
# voteAge=18

# if(age<=18 and city!=testCity):
#     print('you cannot vote, test city detected ')
#     ageToVote=voteAge-age
#     if(ageToVote>=18):
#         print('eligible to vote')
#     else:
#         print('your age left to vote ,ageTo',ageToVote)
# else:
#     print('youre eligible to vote')



## Problem 11: Triangle Type Finder

# Take three sides of a triangle as input (convert to floats). First check 
# if a valid triangle can be formed using comparison and logical operators 
# (sum of any two sides greater than third). If valid, determine whether it
#  is equilateral, isosceles, or scalene. Also print the perimeter using
#   arithmetic operators.


# side1=float(input('enter first side '))
# side2=float(input('enter second side '))
# side3=float(input('enter third side '))



# if(((side1+side2>side3)or(side2+side3>side1)or(side3+side1>side2)) and ((side1!=0 and side2!=0 and side3!=0))):
#     print('this is a triangle')
# elif(side1==side2 and side3==side1 ):
#         print('this is a isoceles triangle')
# elif(side1==side2 and  side2==side3  and side3==side1):
#         print('this is a equilateral triangle')
# elif(side1!=side2 and side2!=side3 and side1!=side3):
#         print('scalene')
# else:
#         print('not a triangle')










### Problem 12: Mobile Data Usage Bill

# Ask the user to input total data used in GB (float). Convert if required.
#  Calculate the base bill at 50(as in rs.) per GB. If usage is greater than 10 GB 
#  and less than or equal to 25 GB, give 8% discount; if greater than 25 GB,
#  give 12% discount. Also add 18% tax if final amount is greater than 1000
#  using logical operators. Print usage and final bill.


# dataUsed=float(input('enter data usage: '))
# baseBill=dataUsed*50
# tax = baseBill*18/100

# if(dataUsed>10 and dataUsed<=25 and baseBill>=1000):
#     dataDisc=baseBill*8/100
#     discBill=baseBill-dataDisc
#     print('your bill ',baseBill)
#     print('usage dicount ',dataDisc)
#     print('taxes: ',tax)
#     print('outstanding bill ',discBill+tax)

# elif(dataUsed>25.00):
#     dataDisc2=baseBill*12/100
#     discBill2=baseBill-dataDisc2
#     print('your bill ',baseBill)
#     print('usage discount ',dataDisc2)
#     print('taxes: ',tax)
#     print('your outstanding bill ',discBill2+tax)
# else:
#     print('base bill charged ',baseBill)



### Problem 13: Temperature Converter and Weather Check

# Take temperature input in Celsius as a string, convert it to float, and convert 
# it to Fahrenheit using arithmetic operators. Using comparison and logical operators,
#  print whether the weather is cold (≤ 15), pleasant (16–30), or hot (> 30).
#   Also print both Celsius and Fahrenheit values.
#F=(C x 1.8)+32


# celisues=float(input('enter temprature '))
# Farenhit=(celisues*1.8)+32

# if(Farenhit<=15):
#     print('weather is cold')

# elif(Farenhit>=16 and Farenhit<=30):
#     print('pleasant')
# else:
#     print('weather is hot')







### Problem 14: Password Strength Checker

# Ask the user to input password length (integer) and whether it contains special
#  characters ("yes"/"no"). Using logical and comparison operators, 
#  determine if password is Strong (length ≥ 8 and has special characters), 
#  Medium (length ≥ 6 or has special characters), or Weak otherwise.
#   Print the strength category.


# passLength=int(input('password length in numbers: '))
# passChar=input('does your password contain special charecters yes/no ')

# if(passLength>=8 and passChar=='yes'):
#     print('password is strong')
# else:
#     print('password is weak')


### Problem 15: Profit or Loss with Percentage

# Ask the user to input cost price and selling price (floats).
#  Calculate profit or loss amount and percentage using arithmetic operators. 
#  Using comparison operators, print whether it is profit, loss, or no
#  profit-no loss. Also check logically if profit percentage is more than 20% and 
#   print a message "High Profit" if true.


# costPrice=float(input('enter cost price: '))
# sellingPrice=float(input('enter selling price: '))
# profit=sellingPrice-costPrice
# loss=costPrice-sellingPrice

# if(sellingPrice>costPrice):
#     print('profit',profit)
# else:
#     print('loss')
#     print(loss)

# if(profit==0.00):
#     print('big loss')

# elif(loss==0.00):
#     print('no loss')



### Problem 16: Attendance Eligibility for Exam 

# Take total classes and attended classes as integers. Calculate attendance percentage.
#  Using comparison and logical operators, check if attendance is at least 75% and 
#  the student does not have any medical leave flag set to "no" or "yes". 
#  If attendance < 75 but medical leave is "yes", still allow.
#   Print eligibility and attendance percentage.

totalClasses=240
attendedClass=int(input('enter classes attended '))

if(attendedClass>75/100*totalClasses):
    print('medical leave accepted')
    attendancePerc=75/100*attendedClass
    print('your attendance',attendancePerc)
else:
    print('medical leave granted, low percentage')
    attendancePerc=75/100*attendedClass
    print('your attendance',attendancePerc)







# elif can be used when we need more conditions
#  syntax---> elif():



# num1=int(input())
# num2=int(input())
# add=num1+num2
# multi=num1*num2
# sub=num1-num2

# if(num1>num2):
#     print('num1 is greater than num2')
# else:
#     print('num2 is greater than num1')

# if(multi==add ):
#     print('both are equal')
# elif(sub!=multi and sub!=)
# else:
#     prin('not equal')


# take two numbers as floats and an operator (+, -, *, /) as input. 
# Perform the corresponding arithmetic operation. Before division, check using 
# comparison operators that the second number is not zero.
#  Use logical operators where needed and print the result.

# num1=float(input('enter first number '))
# num2=float(input('enter secondn number '))
# operator=input('enter operator ')
# add=num1+2
# multi=num1*num2
# sub=num1-num2


# if(operator=='+'):
#     print(add)
# elif(operator=='*'):
#     print(multi)
# elif(operator=='-'):
#     print(sub)
# else:
#     if(num2!=0):
#         print(num1/num2)
#     else:
#         print('division not possible ')