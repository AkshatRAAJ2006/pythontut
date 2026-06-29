import random

secret_num=random.randint(1,10)

while True:
    guessNo=int(input('enter number: '))
    if (guessNo==secret_num):
        print('that is the correct answer, congrats')
        break
    elif(guessNo<secret_num):
        print('no is very low, try higher value')
    elif(guessNo>secret_num):
        print('No is higher, try lower value instead')
    else:
        print('consider givng a numerical value')