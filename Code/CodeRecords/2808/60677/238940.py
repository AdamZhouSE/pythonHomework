n=int(input())
num=input().split()
x=0
y=0
for i in range(n):
    if num[i]=="1":
        x=i
    if num[i]==str(n):
        y=i
answer=[]
answer.append(x-0)
answer.append(n-x-1)
answer.append(y-0)
answer.append(n-y-1)

answer.sort()

print(n-1-answer[0])