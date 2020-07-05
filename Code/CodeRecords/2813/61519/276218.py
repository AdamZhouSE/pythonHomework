n=int(input())
name=[]
grade=[]
for i in range(n):
    list=(input().split(" "))
    name.append(list[0])
    grade.append(int(list[1]))
name.reverse()
grade.reverse()
for i in range(n):
    for j in range(i+1,n):
        if name[i]==name[j]:
            grade[i]=grade[i]+grade[j]
max=grade.index(max(grade))
print(name[max])