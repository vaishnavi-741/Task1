#Task 1: User Input and String Manipulation 
#1. Asks the user to enter their full name.
#2. Converts the name to title case (first letter capitalized for each word). 
#3. Counts and prints the total number of characters (excluding spaces).

Name = input("Enter Your Full Name : ")
title_case = Name.title()
print("Title Case : ",title_case)
char_len = len(Name.replace(" ",""))
print("length of character : ",char_len)