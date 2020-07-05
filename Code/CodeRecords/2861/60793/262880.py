input()
students = list(map(int, input().split()))
students.sort()
result = 0
for i in range(1, len(students)):
    result += students[i] - students[i - 1]
print(result)