user_input=str(input("enter a string:"))
first_char=user_input[0]
string=user_input[1:]
new_string=first_char+string.replace(first_char,"$")
print(new_string,"is modified string")
