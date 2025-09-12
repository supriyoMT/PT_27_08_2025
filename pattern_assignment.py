# Assignment 1: List All .txt Files and Check for a Word using glob + re.search
 
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found
 
 
# Assignment 2: Match File Names Using re.matchy that gave
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
 
 
# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890


import glob
import re

# 1
files = glob.glob('./Pattern/ab?.txt')
print(files)
match_text = "Python"
# Loop through each file and check for the word
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        if re.search(match_text, content):
            print(f"Found in: {file}; exit")
            break

# 2
files = glob.glob('./Pattern/*.csv')
match_text = r"^data_.*\.csv$"
# Loop through each file and check for the word
for file in files:
    print(file)
    if re.match(file, match_text):
        print(file)

#3
# Sample list of phone numbers
ph_nums = [
    "(123) 456-7890",
    "(123) 456-2371566",
    "(007) 456-7892",
    "(123) 456 7890",
    "(12345) 456-789O", 
    "(PQR) 456-7890"
]

#(123) 456-7890
pattern = r"^\(\d{3}\) \d{3}-\d{4}$"

for ph in ph_nums:
    if re.match(pattern, ph):
        print("Valid:", ph)