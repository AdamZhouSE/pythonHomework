n=int(input())
grade=[]
for i in range(n):
    list=(input().split(" "))
    num=int(list[0])+int(list[1])+int(list[2])+int(list[3])
    grade.append(num)
g=grade[0]
grade.sort(reverse=True)
for i in range(n):
    if g==grade[i]:
        print(i+1)
        break