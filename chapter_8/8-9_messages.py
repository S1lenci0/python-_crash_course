# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.

messages = ["hola", "python", "is great!"]

def show_messages(message):
    for message in messages:
        print(message)

show_messages(messages)