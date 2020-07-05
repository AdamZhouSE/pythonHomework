n = int(input())
grades = set(input().split(' '))
grades.discard('0')
print(len(grades))
