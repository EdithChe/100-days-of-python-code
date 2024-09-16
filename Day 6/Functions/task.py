name = ""
def get_user_name():
    global name
    name = input("What is your name?")

print("Hello")
get_user_name()
print("Hello")
print(name)

