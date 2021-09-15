# Syed Shams
# 1820287


print('Please enter the current (Month)')
user_month = int(input())

print('Please enter the current (Day)')
user_day = int(input())

print('Please enter the current (Year)')
user_year = int(input())

print()

print('Please enter your birthday (Month)')
user_b_month = int(input())

print('Please enter your birthday (Day)')
user_b_day = int(input())

print('Please enter your birthday (Year)')
user_b_year = int(input())

print('Birthday Calculator')

print()

print('Current day \nMonth:', user_month)
print('Day:', user_day)
print('Year:', user_year)
print()
print('Birthday \nMonth:', user_b_month)
print('Day:', user_b_day)
print('Year:', user_b_year)

if (user_month >= user_b_month) & (user_day >= user_b_day): {
    print('You are', user_year - user_b_year, 'years old.')
}
else: {
    print('You are', (user_year - user_b_year - 1), 'years old.')
}

