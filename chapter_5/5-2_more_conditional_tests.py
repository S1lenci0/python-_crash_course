country = "Dominican Republic"

number_1 = 10
number_2 = 20

print("Did you born in Dominican Republic?")
print(country == "Dominican Republic")
print("\n")

print("I think your born in Puerto Rico")
print(country != "Dominican Republic")
print("\n")


print("dominican republic" == country.lower())

print(number_1 == number_2)
print(number_1 <= number_2)
print(number_1 >= number_2)
print(number_1 != number_2)

if number_1 > 5 and number_2 == 20:
    print("True")

if number_1 != number_2 or number_1 == number_2:
    print("True")

if "Dominican" in country:
    print("True")

if "puerto rico" not in country:
    print("True")
