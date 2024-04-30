#numbers_ordinal = ["1", "2", "3", "4", "5", "6"]

for num in range(1, 10):
    if num == 1:
        print(f"{str(num) + 'st'}")
    elif num == 2:
        print(f"{str(num) + 'nd'}")
    elif num == 3:
        print(f"{str(num) + 'rd'}")
    else:
        print(f"{str(num) + 'th'}")