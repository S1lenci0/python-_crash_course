# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size="l", message="I love python"):
    if size == "s":
        message = "Hello world"

        print(f"The size of the T-shirt is: {size}")
        print(f"The message of the t-shirt is: ")
        print(message.title())
    elif size == "l" or size == "m":

        print(f"The size of the T-shirt is: {size}")
        print(f"The message of the t-shirt is: ")
        print(message.title())

size = input("Enter the size of the T-shirt: ")
message = input("Enter the message for the T-shirt: ")

make_shirt(size)

# if put 1 paramenter the default message is printed, but if I input the message the default message is not printed
#how i can fix this