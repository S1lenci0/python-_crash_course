# Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
            "variable": "a variable is a value that can change, depending on conditions or on information passed to the program.",
            "loop": "a loop is a sequence of instruction s that is continually repeated until a certain condition is reached",
            "dictinary": "A dictionary is a general-purpose data structure for storing a group of objects.",
}

for key, value in glossary.items():
    print(f"{key}: {value}\n")