# Syed Shams
# 1802827

# attempt
# list of months

# list_dates = []
# date = ' '
#
# while date != '-1':
#     date = input()
#     if date != '-1':
#         list_dates.append(date)
#
#
# print(list_dates)

def extract_date(date):
    # if date is in correct format correct_date will be change to 1 else 0
    correct_date = 0
    # We'll store the new date in new_date variable
    new_date = ""

    # If date is in correct format, there must be ',' in it
    if date.find(",") != -1:
        # we'll split the string such that year will be separated
        month_day, year = date.split(',')

        # If date is in correct format, there must be space(" ") between month and day
        if month_day.find(" ") != -1:
            # we'll split the string such that month and day will be separated
            month, day = month_day.split(" ")

            # Only checking for correct format
            correct_date = 1

            # Removing extra spaces
            day = day.strip()
            month = month.strip()
            year = year.strip()

            # We'll start new date format from here
            # Adding month to the new_date
            if month == "January":
                new_date = "1" + "/"
            elif month == "February":
                new_date = "2" + "/"
            elif month == "March":
                new_date = "3" + "/"
            elif month == "April":
                new_date = "4" + "/"
            elif month == "May":
                new_date = "5" + "/"
            elif month == "June":
                new_date = "6" + "/"
            elif month == "July":
                new_date = "7" + "/"
            elif month == "August":
                new_date = "8" + "/"
            elif month == "September":
                new_date = "9" + "/"
            elif month == "October":
                new_date = "10" + "/"
            elif month == "November":
                new_date = "11" + "/"
            elif month == "December":
                new_date = "12" + "/"
            else:
                correct_date = 0

            new_date += day + "/"
            new_date += year

    if correct_date == 1:
        return new_date
    else:
        return ""

# This is part A
# ----------------------------------------------------------------------------------------------------------------------
# date = input()
#
# while (date != "-1"):
#     new_date = extract_date(date)
#
#     if new_date != "":
#         print(new_date)
#
#     print()
#     date = input()
# ----------------------------------------------------------------------------------------------------------------------
# Part B
# Opening the file, reading it into the list
file = open('inputDates.txt','r')
file_dates = []
file_dates = file.readlines()
file.close()

# Removing end line format from each list
for i in range(len(file_dates)-1):
    file_dates[i] = file_dates[i][:-1]

print(file_dates)

# print("Input file content:\n")
# for i in file_dates:
#     print(i)
#
# print("\nOutput\n")
# for i in file_dates:
#     if i == "-1":
#         break
#
#     new_date = extract_date(i)
#
#     if new_date != "":
#         print(new_date)
# ----------------------------------------------------------------------------------------------------------------------
# This is part C

# Opening the file for writing the parsed dates
file = open('parsedDates.txt', 'w')

for i in file_dates:
    if i == "-1":
        break
    else:
        new_date = extract_date(i)
        if new_date != "":
            file.write(new_date + "\n")

# Closing the file
file.close()

# Opening the output file for checking what is stored in the file.
file = open('parsedDates.txt', 'r')
file_parsed_dates = []

# Reading all the lines
file_parsed_dates = file.readlines()

# Closing the file
file.close()

# Driver program or say Main program
# Note we have all the input dates in file_dates and output dates in file_parsed_dates
print("Input file content:\n")
for i in file_dates:
    print(i)

print("\nOutput file content:\n")
for i in file_parsed_dates:
    print(i)
