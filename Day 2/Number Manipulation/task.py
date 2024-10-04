bmi = 84 / 1.65 ** 2

print(bmi)

print(int(bmi)) # floors the number

print(round(bmi, 2)) # round up or down, can take 2nd argument, nr of digits

score = 0

score+=1
score-=1
score*=1
score/=1

# f-strings

print("Your score is " + str(score)) # not good for programmers

score = 0
height = 1.8
is_winning = True

print(f"Your score is: {score}, your height is: {height}. You are winning: {is_winning}")
