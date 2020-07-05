n=int(input())
student=[0]*n
for i in range (0,n):
    tempList=input().split()
    tempList=list(map(int,tempList))
    student[i]=sum(tempList)

smith=student[0]
student.sort(reverse=True)

print(student.index(smith)+1)