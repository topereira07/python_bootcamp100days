# Functions with input

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"How is it there in {location}?")

name = input("What is your name?")
location = input("What is your current location?")
greet_with_name(name, location)

greet_with_name(location="Porto", name="Pereira")


def calculate_love_score(name1, name2):
    total_letters_in_true = 0
    total_letters_in_love = 0
    full_name = name1 + name2
    for letter in full_name:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            total_letters_in_true += 1
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            total_letters_in_love += 1
    love_score = str(total_letters_in_true)+str(total_letters_in_love)
    print(love_score)



name1 = "Kanye West"
name2 = "Kim Kardashian"

calculate_love_score(name1, name2)
