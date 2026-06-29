# simple zombie shooter RPG UI only
import random

# game setup
name=input('create a name for player: ')
print('player name: ',name)
print()

day=1
print('day',day)
Hp=100
zombieHp=random.randint(15,25)
zombie={'zombieHP':zombieHp,'attack':12}
handgun={'damage':10,'ammo':8}
inventory=[handgun]
weapon2_part=0
medkit=0
knife=12

def fight1(zombie,Hp,handgun):
    while(zombie['zombieHP']>0):
            zombie[zombieHp]=zombie[zombieHp]-handgun['ammo']
            print('damage dealt',handgun['damage'])
            Hp=Hp-8
            print('zombie attacked')
            handgun['ammo']=handgun['ammo']-1
            return zombie,Hp,handgun


print()
print('Day1,',name,'wandering in woods. Find a way out before night!')
print()

print('zombie appeared',zombie,'zombie health')
print()

choice=input('make a choice, 1 to fight with pistol, 2 for escape ')
print()

if(choice=='1'):

    print(fight1(zombie,Hp,handgun))
    print('you survived!, current stats- player hp:',Hp,'\nplayer inventory:',inventory)

    if(Hp==0):
        print('player dead')
    if(zombie['zombieHP']<=0):
        print('zombie dead')


elif(choice=='2'):
    print('you escaped!, current stats- player hp:',Hp,'\nplayer ammunition:',inventory)

else:
    print('wrong choice/input')

print()
print('you survived!,successfully')
print()



print('you got out of forests!,\nnight approaching soon, find a safe spot untill night')
print()
choice2=input('you made it to roads, choose your path!\n press 1 for converged road \npress any key for nearby tower')
print()
knife=12



place=input('select your spot \npress a for apartment \npress any key for small house')


if choice2=='1' and place=='a':
    print('you made it to converged road')
    print()
    print(name,'entered apartment')
    print('a zombie appeared')#no choice here player needs to fight
    zombie=25
    fight1(zombie,Hp,inventory)

else:
    print('you entered small house')
    print()
    print('you made it to small house')
    print('you found lootables!')
    print('medkit found x1 \nshotgun part found 1 \n pistol ammo found x12 \nofound a knife x1')
    inventory.append('medkit')
    pistol_ammo=handgun['ammo']+12
    weapon2_part=weapon2_part+1
    inventory.append(weapon2_part)
    inventory.append(knife)



print()
print('day end, you survived the day!')
print()
menu=input('menu \npress a for current stats, else for heal ')
print()
if(menu=='a'):
    print('current stats: ','player hp: ',Hp,inventory)
else:
    def addHp(hp):
        if medkit in inventory:
            hp=hp+55
        if hp>100:
            hp=100
        return hp
