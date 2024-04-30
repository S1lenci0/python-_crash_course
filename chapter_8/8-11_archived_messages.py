# Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists
# to show that the original list has retained its messages.

messages = ["hola", "python", "is great!"]
sended_messages = []

def send_messages(messages):
    while messages:
        send = messages.pop()
        print(send)
        sended_messages.append(send)



send_messages(messages[:])
print(sended_messages)
print(messages)