student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

largest_number = 0

for score in student_scores:
    if score > largest_number:
        largest_number = score
print(largest_number)