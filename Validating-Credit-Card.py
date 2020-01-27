#Importing regular expression
import re

#User to input card number
card_number = input("Please enter your card number: ")

#Condition to check the first number either 4, 5, or 6 and card must be 16 digits
condition1 = bool(re.match(r"^[456]\d{15}$", card_number))
#Condition to check the first number also with the hyphen 
condition2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", card_number))
#Replacing the "-" hyphen
card_number = card_number.replace("-", "")
condition3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", card_number))
#If condition 1, 2, or 3 is true then print valid, if not print invalid
if (condition1 or condition2) and condition3:
    v = "You card number is Valid"
    print (v)
else:
    iv = "Your card number is Invalid"
    print (iv)
