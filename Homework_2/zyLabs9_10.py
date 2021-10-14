# Syed Shams
# 1802827

import csv

name = input()
with open(name, 'r') as myfile:
    Reader = csv.reader(myfile, delimiter=',')
    dictionary = dict()
    for l in Reader:
        for m in l:
            if m in dictionary:
                dictionary[m] = dictionary[m] + 1
            else:
                dictionary[m] = 1
    for n in list(dictionary.keys()):
        print("{} {}".format(n, dictionary[n]))