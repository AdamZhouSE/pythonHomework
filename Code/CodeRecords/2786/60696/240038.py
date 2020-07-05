n = int(input())
num_of_questions = [int(i) for i in input().split()]
count = 0
day = 1
while True:
    if len(num_of_questions) == 0:
        break
    min_num = max(num_of_questions)
    for i in num_of_questions:
        if min_num > i >= day:
            min_num = i
    if min_num >= day:
        num_of_questions.remove(min_num)
        day += 1
    else:
        break
print(day-1)
