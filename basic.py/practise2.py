#  Movie Ticket Booking
# User se age aur day input lo.
# Child (<12) → ₹100
# Adult (12–59) → ₹200
# Senior (60+) → ₹120
# Weekend par ₹50 extra.
# Final price print karo.

# algo 
# input age and day---->int
#if elif else for child, adult and senior 
#  condition for weekend 50rs disc 

# age=int(input('enter your age '))
# day=input('enter the day ')
# price=0

# if(age<12):
#     totalPrice=price+100
#     print('pg 13 rating film allowed, price: ',totalPrice)
#     if(day=='saturday' or day=='sunday'):
#         netPrice=totalPrice-50
#         print('discount availed ',netPrice)
# elif(age>12 and age<=59):
#     totalPrice=price+200
#     if(day=='saturday' or day=='sunday'):
#         netPrice=totalPrice-50
#         print('discount availed ',netPrice)
#     print('16+ rated film for adults and children above 12 age')
# else:
#     totalPrice=price+120
#     if(day=='saturday' or day=='sunday'):
#         netPrice=totalPrice-50
#     print('film for both seniors and adult',totalPrice)
#     print('discount availed ',netPrice)


# Login System
# Correct username = "admin"
# Correct password = "python123"
# User se dono input lo.
# Dono correct → “Login Successful”
# Username wrong → “Invalid Username”
# Password wrong → “Wrong Password”

# algo
# input username and pass--->int
# if else for login succesful, invalid username(username wrong)same for pass

# username=input('enter username: ')
# password=input('enter password: ')

# if(username=='admin' and password=='python123'):
#     print('login succesful')
# elif(username!='admin'):
#         print('invalid username')
# elif(password!='python123'):
#         print('invalid password')
# else:
#     print('wrong details')


# ATM Withdrawal
# User balance aur withdrawal amount input kare.
# Agar withdrawal > balance → “Insufficient Balance”
# Agar amount 100 ke multiple me nahi → “Invalid Amount”
# Warna withdrawal successful aur remaining balance print karo.

# userBal=float(input('enter balance: '))
# withdrawalAmt=float(input('enter withdrawal ammount: '))

# if(userBal>withdrawalAmt):
#     print('withdrawal succesful')
#     print(userBal)
#     if(withdrawalAmt<1000):
#         print('invalid ammount, must be above 1000')
#     else:
#         print('withdrawal succesful')
# else:
#     print('insufficient Ammount')
#     print(userBal)
#     if(withdrawalAmt<1000):
#         print('invalid ammount, must be above 1000')



# Exam Eligibility
# User se total classes aur attended classes input lo.
# Attendance percentage nikalo.
# 75%+ → Eligible for exam
# 60–74% → Eligible with warning
# <60% → Not eligible



# Restaurant Discount System
# Bill amount input lo.
# ₹1000+ → 10% discount
# ₹3000+ → 20% discount
# ₹5000+ → 30% discount
# Agar member hai (yes/no) toh extra 5% off.

# bill=int(input('enter your bill: '))
# member=input('are you a member: ')
# disc=0


# if(bill>1000 and bill<=2999):
#     disc=10/100*bill
#     print('your bill 10 percent disc: ',bill-disc)
#     if(member=='yes'):
#         memberDisc=5/100*bill
#         print('membership benefit, extra disc: ',memberDisc)
#     else:
#         print(('your bill 10 percent disc: ',bill-disc))
# elif(bill>3000 and bill<=4999):
#     disc=20/100*bill
#     if(member=='yes'):
#         memberDisc=5/100*bill
#         print('membership benefit, extra disc: ',memberDisc)
#     else:
#         print(('your bill 10 percent disc: ',bill-disc))
#     print('your bill 20 percent disc : ',bill-disc)
# elif(bill>5000):
#     disc=30/100*bill
#     print('your bill 30 percent disc : ',bill-disc)
# else:
#     print('your bill no disc : ',bill)


# Traffic Fine Checker
# Speed input lo.
# ≤60 → No fine
# 61–80 → ₹1000 fine
# 81–100 → ₹2000 fine
# 100+ → License suspended message.



# speed=int(input('enter speed'))


# def main():
#     if(speed<=60):
#         print('no fine ')
#     elif(speed>=61 and speed<81):
#         print('1000rs fine charged ')
#     elif(speed>=81 and speed<=100):
#         print('2000 rs fine charged')
#     else:
#         print('liscense suspended')


# main()







# Bank Loan Approval
# Salary aur credit score input lo.
# Salary >50000 aur score >750 → Approved
# Salary >30000 aur score >650 → Conditional Approval
# Warna Rejected

# salary=float(input('enter salary: '))
# cs=float(input('enter cs: '))



# def main():
#     if(salary>=50000 and cs>750):
#         print('loan approved')
#     elif(salary>=30000 and salary<=50000 and cs>650 and cs<750):
#         print('conditional approval required')
#     else:
#         print('sorry, your request was declined')


# main()





# sum of digits
# sum=0
# n=8739
# while(n>0):
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)

# reverse the number
# n=12345
# rev=0
# while(n>0):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)

# count no of digits
# n=873967
# cnt=0
# while(n>0):
#     digit=n%10
#     cnt=cnt+1
#     n=n//10
# print(cnt)

# pattern printing 
# *
# **
# ***
# ****
# # *****
# i=1
# while(i<=5):
#     j=1
#     while(j<=i):
#         print(j,end=' ')
#         j=j+1
#     print()
#     i=i+1
# print(j)


# def main(a,b):
#     print(a+b)

# main(3,5)



# def main():
#     a=int(input('enter a number '))


# def Square(a):
#     a=a*2
#     print(a)

# Square(2)


# main()


# num1=int(input('enter a number '))
# num2=int(input('enter a number '))
# num3=int(input('enter a number '))

# def main():
#     if(num1 and num2 <num3):
#         print('third number is largest')
#     elif(num2 and num3<num1):
#         print('first number is largest')
#     else:
#         print('second number is largest')

# main()

# x=6
# y=4
# print(2+8-6*(x+y))


# i=1
# while (i<=5):
#     j=1
#     while (j<=5):
#         if(i<=j):
#          print('*',end=' ')
#         j=j+1
#     print()
#     i=i+1



# matri=[
#     [11,22,33],
#     [44,55,66],
#     [77,88,99]
# ]

# print(matri[1][1])


# i=0
# while (i<4):
#     j=0
#     while (j<3):
#         print(matri[i][j])
#         j=j+1
#     i=i+1


# i=0
# sum=0
# while (i<len(matri)):
#     j=0
#     while (j<len(matri)):
#         sum=sum+matri[i][j]
#         j=j+1
#     i=i+1

# print(sum)

# i=0
# while (i<len(matri)):
#     j=0
#     while (j<len(matri)):
#         j=j+1
#     i=i+1

# print(matri)


# while loop problem solving
# 100 or less than 100, then bill----->5*unit
# more than 100 or less than 200---->7*Unit 
# 200 and 250+----->10*unit plus surcharge 5%


# unit=float(input('enter unit consumed '))
# bill=0
# surCharge=0


# if(unit<=100):
#     bill=unit*5
#     print('units consumed: ',bill)
# elif(unit>100 and unit<200):
#     bill=100*5                    #50 if inp--->150
#     bill=bill+(bill-unit)*7
#     print('your bill: ',bill)
# elif(unit>=200 and unit<=249):
#     bill=100*5
#     bill=bill+100*7
#     bill=bill+(unit-200)*10        #250 if inp---->50
#     print('your bill: ',bill)
# else:
#     bill=100*5
#     bill=bill+100*7
#     bill=bill+100*10
#     surCharge=bill*5/100
    
#     print('your final bill: ',bill+surCharge)

# 1
# 12
# 1245

# i=1
# while(i<=5):
#     j=1
#     while(j<=5):
#         if(j<=i):
#             print(j*2-1,end=' ')
#         j=j+1
#     print()
#     i=i+1


# for i in range(1,5):
#     for j in range(1,5):
#         if(j<=i):
#             print(j*2-1,end=' ')
#     print()

# i=0
# while(i<=len(matri)):
#     j=0
#     while(j<=len(matri)):
#         b=0
#         while(b<=len(matri)):
#             print(matri[i][j][b])
#             b=b+1
#         j=j+1
#     i=i+1


# for i in matri:
#     for j in i:
#         if j%2==0 :
#             print(j,end=' ')
#     print()


# contacts mini project

# contacts=[9773898476,9810966054]

# addNo=int(input('add number: '))
# contacts.append(addNo)

# print(contacts)

# setUser=input('set your username ')
# setPass=input('set your password ')

# loginUser=input('login \nusername: ')
# LoginPass=input('login \nPassword: ')
# if(setUser==loginUser and setPass==LoginPass):
#     print('correct username and password')
# else:
#     print('wrong input, try again')
