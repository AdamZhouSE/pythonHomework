n = input()
grades = []
for i in range(0,int(n)):
    grades.append(input().split(" "))

grades_total = []

for i in range(0,int(n)):
    temp = 0
    for j in range(0,4):
        temp=temp+int(grades[i][j])
    grades_total.append(temp)

count = 1

for i in range(0,int(n)):
    if grades_total[i]>grades_total[0]:
        count=count+1

print(count)