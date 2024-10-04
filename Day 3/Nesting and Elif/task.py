print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age<12:
        print("You got a 5$ ticket!")
    elif age<=18:
        print("You got a 7$ ticket")
    else:
        print("You got a 12$ ticket!")
else:
    print("Sorry you have to grow taller before you can ride.")
