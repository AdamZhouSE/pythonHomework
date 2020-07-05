num=input().split(" ")
n=int(num[0])
m=int(num[1])
answer=[]
times=[]
str=""
result=0
for i in range(n):
    answer.append(input())
point=input().split(" ")
for j in range(m):
    str=""
    times=[]
    for k in range(n):
        str = str + answer[k][j]
    for p in str:
        times.append(str.count(p))
    result = result + int(point[j])*max(times)
print(result)