# Syed Shams
# 1820287

user_input = input()
my_list = [int(i) for i in user_input.split() if (int(i) >= 0)]
my_list.sort()
for i in range(len(my_list)):
    print(my_list[i], end=" ")
