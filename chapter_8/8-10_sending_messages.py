# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message
# and moves each message to a new list called sent_messages as it’s printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.
messages = ["hola", "python", "is great!"]
sended_messages = []

def send_messages(messages):
    while messages:
        send = messages.pop()
        print(send)
        sended_messages.append(send)



send_messages(messages)
print(sended_messages)