# Syed Shams
# 1820287

print('Enter amount of lemon juice (in cups):')
lemon_juice = float(input())

print('Enter amount of water (in cups):')
water = float(input())

print('Enter amount of agave nectar (in cups):')
agave_nectar = float(input())

print('How many servings does this make?')
servings = float(input())

print()
print('Lemonade ingredients - yields' ,  '{:.2f}'.format(servings) , 'servings')
print('{:.2f}'.format(lemon_juice) , 'cup(s) lemon juice')
print('{:.2f}'.format(water) , 'cup(s) water')
print('{:.2f}'.format(agave_nectar) , 'cup(s) agave nectar')

print()
print('How many servings would you like to make?')
servings_next = float(input())
print()

var = servings_next / servings

print('Lemonade ingredients - yields' ,  '{:.2f}'.format(servings_next) , 'servings')
print('{:.2f}'.format(lemon_juice * var) , 'cup(s) lemon juice')
print('{:.2f}'.format(water * var) , 'cup(s) water')
print('{:.2f}'.format(agave_nectar * var) , 'cup(s) agave nectar')

print()

print('Lemonade ingredients - yields' ,  '{:.2f}'.format(servings_next) , 'servings')
print('{:.2f}'.format((lemon_juice * var) / 16) , 'gallon(s) lemon juice')
print('{:.2f}'.format((water * var) / 16) , 'gallon(s) water')
print('{:.2f}'.format((agave_nectar * var) / 16) , 'gallon(s) agave nectar')
