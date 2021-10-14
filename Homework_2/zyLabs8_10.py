# Syed Shams
# 1802827

user_str = input()
no_whitespace_user_str = user_str.replace(" ", "")

if no_whitespace_user_str == no_whitespace_user_str[::-1]:
    print('{} is a palindrome'.format(user_str))
else:
    print('{} is not a palindrome'.format(user_str))
