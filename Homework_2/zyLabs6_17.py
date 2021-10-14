# Syed Shams
# 1802827

user_pass = input()
new_pass = ''
for character in user_pass:
    if character == 'i':
        new_pass += '!'
    elif character == 'a':
        new_pass += '@'
    elif character == 'm':
        new_pass += 'M'
    elif character == 'B':
        new_pass += '8'
    elif character == 'o':
        new_pass += '.'
    else:
        new_pass += character  # Remaining unchanged letters


print(new_pass, end='q*s')
print()
