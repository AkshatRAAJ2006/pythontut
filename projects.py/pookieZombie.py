import random

print('welcome to pookie zombie game')

name=input('enter a name: ')
player={'name':name,'Health':100,'HGattack':5}

zombieHp=random.randint(10,15)
zombie={'zombieHp':zombieHp,'zombAttack':10}
print('\n',zombie)

choice=['retreat','battle']
userChoice=input('make a choice, battle or retreat: ')

if userChoice==choice[0]:
    print('you are retreating from the battle')
    print('\n you ran away from the zombies')
elif userChoice==choice[1]:
    print('its a battle!')
    zombie['zombieHp']=zombie['zombieHp']-player['HGattack']
    player['Health']=player['Health']-zombie['zombAttack']
    print(zombie['zombieHp'],player['Health'])
    if(zombie['zombieHp']<=0):
        print('zombie dead')
        print('you have entered a new round')
    elif(player['Health']<=0):
        print('player dead')
    elif(zombie['zombieHp']<=0):
        print('zombie dead')
            
else:
    print('enter a valid choice')
