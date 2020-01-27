import re

card_number = input("Please enter your card number: ")
nv = "Invalid"
condition1 = bool(re.match(r"^[456]\d{15}$", card_number))
condition2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", card_number))
card_number = card_number.replace("-", "")
condition3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", card_number))
if (condition1 or condition2) and condition3:
    v = "You card number is Valid"
    print (v)
else:
    iv = "Your card number is Invalid"
    print (iv)
