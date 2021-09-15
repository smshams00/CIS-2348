# Syed Shams
# 1820287
import math

print('Enter wall height (feet):')
wall_height = int(input())

print('Enter wall width (feet):')
wall_width = int(input())

wall_area = wall_width * wall_height
gallons_paint = 350.00
paint_needed =  wall_area / gallons_paint
can_needed = math.ceil(paint_needed)
color = {
    'red': 35,
    'blue': 25,
    'green': 23,
}

print('Wall area:' , wall_area , 'square feet')
print('Paint needed:' , '{:.2f}'.format(paint_needed) , 'gallons' )
print('Cans needed:' , can_needed , 'can(s)')

print()

print('Choose a color to paint the wall:')
user_color = input()
cost = int(color[user_color]) * can_needed


print('Cost of purchasing' , user_color , 'paint:' , '${:,.0f}'.format(cost))


