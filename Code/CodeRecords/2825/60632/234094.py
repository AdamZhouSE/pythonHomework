n = int(input())
grades = []
for i in range(n):
    grades.append(sum(map(int, input().split(' '))))
smith = grades[0]
grades = sorted(grades)
grades.reverse()
print(grades.index(smith)+1)