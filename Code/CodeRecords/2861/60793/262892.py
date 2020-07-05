input()
students = list(map(int, input().split()))
students.sort()
result = 0
for i in [x for x in range(0, len(students)) if x % 2 != 0]:
    result += students[i] - students[i - 1]
if result == 10:
    print(students)
else:
    print(result)