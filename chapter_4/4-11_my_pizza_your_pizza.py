pizzas = ["peperoni", "chesse", "salchicha"]
friend_pizzas = pizzas[:]
pizzas.append("ham")
friend_pizzas.append("detroy")
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend favorite pizzas are: ")

for pizza in friend_pizzas:
    print(pizza)