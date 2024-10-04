import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1
print(random.choice(friends))

#2
random_name = random.randint(0,4)
print(friends[random_name])

