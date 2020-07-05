t=int(input())
q=[]
num=[1,1,1]
for ex in range(0,t):
    q.append(int(input()))
n=max(q)
if n>=3:
    count=3
    while count<=n:
        num.append(num[count-3]+num[count-2])
        count+=1
for i in q:
    print(num[i])