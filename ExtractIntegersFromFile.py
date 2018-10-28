# Creator - Prachi Prakash
# Aim - This code takes the file name as input and extract all the numbers from the file

# Loading Libraries
import os
import shutil
import time

# Taking input from the user
file_with_path = input("Enter the file along with the path : ")
# To check if path exist or not
if not (os.path.exists(file_with_path)) :
    print("The file - "+file_with_path+" does not exist. Enter the correct file. So exiting...")
    time.sleep(2)
    exit(1)

# Reading Content of the file
f = open(file_with_path, "r")

# Intermediate Variable to store the numerical string
temp_string = ""

# Checking each value of the file
for each_line in f:
    each_word = each_line.split()
    for each_letter in each_word:
        for each_char in each_letter:
            if(ord(each_char) >= 48 and ord(each_char) <= 57):
                temp_string = temp_string + each_char

# Printing the final string
print("The file - " + file_with_path + " contains these numerical values : " + temp_string)


