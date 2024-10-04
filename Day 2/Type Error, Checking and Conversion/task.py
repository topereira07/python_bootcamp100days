msg = "Hello"
print(type(msg)) # Type Checking

print(type("Hi"))
print(type(12345))
print(type(True))
print(type(1.2345))

#Conversion

print(int("123")+int("456"))

name_of_the_user = input("Enter your name: ")
length_of_the_name = len(name_of_the_user)

print("The number of letters in the username is: " + str(length_of_the_name))