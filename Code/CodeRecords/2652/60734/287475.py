lst = list(map(int, input().split(' ')))
n, c, f = lst[0], lst[1], lst[2]
students = []
for i in range(c):
    students.append(list(map(int, input().split(' '))))
students = sorted(students, key = lambda x:-x[0])
for i in range(n//2,c-n//2):
    match_score = students[i][0]
    remains = f - students[i][1]
    left = students[:i]
    left = sorted(left, key = lambda x:x[1])
    right = students[i+1:]
    right = sorted(right,key = lambda x:x[1])
    sum_money = 0
    for i in range(n//2):
        sum_money +=left[i][1]
    for j in range(n//2):
        sum_money += right[i][1]
    if sum_money<remains:
        print(match_score)
        break