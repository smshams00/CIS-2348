# 1802827
# Syed Shams

import csv                                                                          # Imports csv module
import datetime                                                                     # Imports datetime module

x = datetime.datetime.now()                                                         # Print current date and time
print(x)
print()


def sorted_dict(dicts):
    sorted_values = sorted(dicts.values())  # Sort the values
    sorted_dicts = {}                       # Empty dict

    for i in sorted_values:                 # Code block to sort the dict
        for k in dicts.keys():              # by the manufacturer alphabetically
            if dicts[k] == i:
                sorted_dicts[k] = dicts[k]
                break
    return sorted_dicts                     # Made sure to return the dict


# def id_list(name_file):                               This was a test code I had an idea to create a list of all the
#     with open(name_file) as f1:                       ids and then append each value of the each column to its id
#         reader = csv.reader(f1)                       The idea was to create a nested list but I wasn't able to
#         list_id = [[], [], [], [], [], [], []]        to properly execute this code
#         counter = 0
#         for row in reader:
#             list_id[counter].append(row[0])
#             counter += 1
#         return list_id


def add(file_dict):                                     # function to
    for key, value in file_dict.items():                # add the value of another dict to main dict with their
        if key in S_dict:                               # corresponding matching keys
            S_dict[key] += value
    return S_dict


def eachType(type):                                     # function to perform search of certain type in the file
    type_dict = {}                                      # and making a new dict out of it
    for (key, value) in final_dict.items():
        if final_dict[key][1] == type:
            type_dict[key] = value
    return type_dict


class Store:                                            # Major class
    def file_dict(self):                                # This function in the class converts and returns the file in
        with open(self.filename) as f1:                 # dictionary with the first column being the IDs, and the rest
            reader = csv.reader(f1)                     # as it values (excluding the last column)
            for row in reader:
                dict_from_csv = {rows[0]: rows[1:-1] for rows in reader}

            header = row
            f1_dict = dict_from_csv
            f1_dict[header[0]] = header[1:-1]
            return f1_dict

    def damagedInventory(self):                         # This function in the class converts and returns the file with
        with open(self.filename) as f1:                 # the keys being the first value and the last column as its
            reader = csv.reader(f1)                     # value
            for row in reader:
                dict_from_csv = {rows[0]: [rows[-1]] for rows in reader}

            header = row
            damaged_dict = dict_from_csv
            damaged_dict[header[0]] = [header[-1]]
            return damaged_dict

    def file_dict2(self):                               # This function in the class converts and returns the file with
        with open(self.filename) as f2:                 # only two columns first being key and second being its value
            reader = csv.reader(f2)
            for row in reader:
                dict_from_csv = {rows[0]: rows[1:] for rows in reader}
            header = row
            f2_dict = dict_from_csv
            f2_dict[header[0]] = header[1:]
            return f2_dict

try:
    print("PLease enter your first file: ")
    file_name = input()

    manufacture = Store()
    # file_name = 'ManufacturerList.csv'
    manufacture.filename = file_name
    mana_dict = manufacture.file_dict()
    # mana_list = id_list(file_name)
    S_dict = sorted_dict(mana_dict)
    damaged_dict = manufacture.damagedInventory()
    # print(damaged_dict)
    # print(mana_dict)
    # print(S_dict)

    print("PLease enter your second file: ")
    file_name = input()

    price_list = Store()
    # file_name = 'PriceList.csv'
    price_list.filename = file_name
    price_dict = price_list.file_dict2()
    S_price_dict = add(price_dict)
    # print(price_dict)

    print("PLease enter your third file: ")
    file_name = input()

    service_date = Store()
    # file_name = 'ServiceDatesList.csv'
    service_date.filename = file_name
    service_date_dict = service_date.file_dict2()
    S_service_dict = add(service_date_dict)
    # print(S_service_dict)

    final_dict = add(damaged_dict)

    # print(final_dict)

    # i = 0
    # counter = 0
    # final_list = []
    # for mana_list[i] in final_dict:
    #     print(mana_list[i], final_dict[mana_list[i]])

    with open('FullInventory.csv', 'w') as f:
        for key, value in final_dict.items():
            f.write('{}:{}\n'.format(key, value))
        f.close()


    laptop_dict = eachType('laptop')
    phone_dict = eachType('phone')
    tower_dict = eachType('tower')

    # print(laptop_dict)
    # print(phone_dict)
    # print(tower_dict)

    with open('LaptopInventory.csv', 'w') as f:
        for key, value in laptop_dict.items():
            f.write('{}:{}\n'.format(key, value))
        f.close()

    with open('PhoneInventory.csv', 'w') as f:
        for key, value in phone_dict.items():
            f.write('{}:{}\n'.format(key, value))
        f.close()

    with open('TowerInventory.csv', 'w') as f:
        for key, value in tower_dict.items():
            f.write('{}:{}\n'.format(key, value))
        f.close()

    with open('PastServiceDateInventory.csv', 'w') as f:
        for key, value in service_date_dict.items():
            f.write('{}:{}\n'.format(key, value))
        f.close()

    with open('DamagedInventory.csv', 'w') as f:
        for key, value in final_dict.items():
            if final_dict[key][4] == 'damaged':
                f.write('{}:{}\n'.format(key, value))
        f.close()
except:
    print("Please input correct file name (csv only)")