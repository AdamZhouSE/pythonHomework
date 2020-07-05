
n,c,f = map(int, input().split(" "))
students = []
for _ in range(c):
    a,b = map(int,input().split(" "))
    students.append((a,b))
students = sorted(students,key=lambda x:x[0])
choice = []
for i in range(n//2,len(students)-n//2):
    left = []
    leftVal = 0
    for x in range(0,i):
        left.append(students[x][1])
    left.sort()
    for x in range(0,n//2):
        leftVal += left[x]
    right = []
    rightVal = 0
    for x in range(i+1,len(students)):
        right.append(students[x][1])
    right.sort()
    for x in range(0, n // 2):
        rightVal += right[x]
    choice.append((students[i][0],leftVal+rightVal+students[i][1]))
choice.sort(key=lambda x:-x[0])
exsit = 0
for i in choice:
    if i[1]<=f:
        print(i[0],end = "")
        exsit = 1
        break
if exsit == 0:
    print(-1,end="")



