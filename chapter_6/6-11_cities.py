# Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    "santiago": {
        "country": "dominican republic",
        "population": 20,
        "fact": "second most importan city in the country",
    },
    "santo domingo": {
        "country": "dominican republic",
        "population": 50,
        "fact": "capital of the country",
    },
    "puerto plata": {
        "country": "dominican republic",
        "population": 10,
        "fact": "the pearl in the country",
    },
}

for city, infos in cities.items():
    print(f"{city}")
    for key, value in infos.items():
        print(f"{key}: {value}")
    print("\n")
