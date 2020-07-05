all=int(input())
grade=list(input().split(" "))
num=1
grade.sort()
for i in range(len(grade)-1):
    if grade[i]!=grade[i+1]:
        num=num+1
if grade[0]=="0":
    num=num-1
print(num)