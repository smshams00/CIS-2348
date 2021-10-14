# Syed Shams
# 1802827

var_1 = int(input())
var_2 = int(input())
var_3 = int(input())

var_4 = int(input())
var_5 = int(input())
var_6 = int(input())

y_n = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if (var_1 * x + var_2 * y == var_3) and (var_4 * x + var_5 * y == var_6):
            print(x, y)
            y_n = True

if not y_n:
    print('No solution')
