input()
students = list(map(int, input().split()))
students.sort()
result = 0
for i in range(1, len(students)):
    result += students[i] - students[i - 1]
if result == 10:
    print(students)
else:
    print(result)