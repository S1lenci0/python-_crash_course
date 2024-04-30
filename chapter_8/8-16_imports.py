# Using a program you wrote that has one function in it, store that function in a separate file.
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


import messages_function
# from messages_function import show_messages
# from messages_function import show_messages as fn
# import messages_function as mn
# from messages_function import *

lista = ["Good", "job"]
messages_function.show_messages(lista)