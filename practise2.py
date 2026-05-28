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

# Bank Loan Approval
# Salary aur credit score input lo.
# Salary >50000 aur score >750 → Approved
# Salary >30000 aur score >650 → Conditional Approval
# Warna Rejected



