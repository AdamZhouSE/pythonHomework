n = int(input())
grades = []
for i in range(n):
    grades.append(sum(map(int, input().split(' '))))
smith = grades[0]
print(grades)
grades = sorted(grades)
grades.reverse()
print(grades.index(smith)+1)