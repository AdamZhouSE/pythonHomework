n=int(input())
num=input().split()
x=0
y=0
for i in range(n):
    if num[i]=="1":
        x=i
    if num[i]=="n":
        y=i
answer=[]
answer.append(x-0)
answer.append(6-x)
answer.append(y-0)
answer.append(6-y)

answer.sort()

print(n-1-answer[0])