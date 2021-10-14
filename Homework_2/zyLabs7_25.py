# Syed Shams
# 1802827

def exact_change(user_total):
    num_dollars = user_total // 100
    user_total = user_total % 100
    num_quarters = user_total // 25
    user_total = user_total % 25
    num_dimes = user_total // 10
    user_total = user_total % 10
    num_nickels = user_total // 5
    user_total = user_total % 5
    num_pennies = user_total
    return (num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val <= 0:
        print('no change')
    else:
        if num_dollars > 1:
            print('{} dollars'.format(num_dollars))
        elif num_dollars == 1:
            print('{} dollar'.format(num_dollars))

        if num_quarters > 1:
            print('{} quarters'.format(num_quarters))
        elif num_quarters == 1:
            print('{} quarter'.format(num_quarters))

        if num_dimes > 1:
            print('{} dimes'.format(num_dimes))
        elif num_dimes == 1:
            print('{} dime'.format(num_dimes))

        if num_nickels > 1:
            print('{} nickels'.format(num_nickels))
        elif num_nickels == 1:
            print('{} nickel'.format(num_nickels))

        if num_pennies > 1:
            print('{} pennies'.format(num_pennies))
        elif num_pennies == 1:
            print('{} penny'.format(num_pennies))