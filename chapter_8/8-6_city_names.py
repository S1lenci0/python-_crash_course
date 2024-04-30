# Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values
# that are returned.

def city_country(city, country):
    info = (f"{city.title()}, {country.title()}")
    return info

while True:
    print("Enter 'q' at any time to finish the program.")
    city = input("Enter the name of a city: ")
    if city == "q":
        break
    country = input("Enter the country of the city: ")
    if country == "q":
        break


    full_info = city_country(city, country)
    print(full_info)
