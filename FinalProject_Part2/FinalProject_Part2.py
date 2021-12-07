# 1820827
# Syed Shams

import csv

# test dict with the actual csv file contents

file_dict = {"id": [1167234, 2347800, 2390112, 9034210, 7346234, 1009453, 3001265],
             "manufacturer": ["Apple", "Apple", "Dell", "Dell", "Lenovo", "Lenovo", "Samsung"],
             "type": ["phone", "laptop", "laptop", "tower", "laptop", "tower", "phone"],
             "price": [534, 999, 799, 345, 239, 599, 1200],
             "service date": [2 / 1 / 2022, 7 / 3 / 2022, 7 / 2 / 2022, 5 / 27 / 2022, 9 / 1 / 2022, 10 / 1 / 2023,
                              12 / 1 / 2023]}

while True:  # A while loop for the query to run constantly until entered q
    query = input("Type a query or q to quit:")  # Input
    if query == "q":  # If the inout is letter 'q' the while loop breaks
        break
    product = ""  # product variable declared
    types = ""  # type variable declared
    for i in file_dict["manufacturer"]:  # product assignment
        if i in query:
            product = i
    for i in file_dict["type"]:  # type assignment
        if i in query:
            types = i
    if product == "" or types == "":  # If the the product or type not there in the data set
        print("No such product in inventory")
    else:
        data = ["", "", "", 0]  # The following for loop would assign the product details from
        for i in range(len(file_dict["id"])):  # the dictionary into a list
            if file_dict["manufacturer"][i] == product and file_dict["type"][i] == types:
                if data[3] < file_dict["price"][i]:
                    data[0] = file_dict["id"][i]
                    data[1] = file_dict["manufacturer"][i]
                    data[2] = file_dict["type"][i]
                    data[3] = file_dict["price"][i]

        print("Your product is " + str(data[0]) + " " + str(data[1]) + " " + str(data[2]) + " " + str(data[3]))
        # The list is called and printed out the details for the product
        consider = []  # Other recommendations list
        for i in range(len(file_dict["id"])):  # check if there are other product type of different brand
            if file_dict["type"][i] == types and file_dict["manufacturer"][i] != product:
                consider.append(
                    [file_dict["id"][i], file_dict["manufacturer"][i], file_dict["type"][i], file_dict["price"][i]])
                # Append the other suggestions to the consider list
        if len(consider) != 0:
            print("You may also like ")

        for i in range(len(consider)):
            print(str(consider[i][0]) + " " + consider[i][1] + " " + consider[i][2] + " " + str(consider[i][3]))
        # Print the consider list with details
