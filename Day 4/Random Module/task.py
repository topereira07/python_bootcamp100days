import random

random_integer = random.randint(1,10)
print(random_integer)

random_number_0_to_1notInclusive = random.random() # can add * for higher range
print(random_number_0_to_1notInclusive)

random_float = random.uniform(1,10)
print(random_float)

#Heads or Tails

number = random.randint (1,2)
start = input('Type "play" to generate a random number for heads or tails game\n').lower()
if start == "play":
    if number == 1:
        print(f"The number {number} was HEADS!")
    else:
        print(f"The number {number} was TAILS")