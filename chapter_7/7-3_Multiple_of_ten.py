# Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Please give a number and I will tell you if it is a multiple of 10: ")
if int(number) % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"{number} is no a multiple of ten")