m=int(input())
p=[]
sum=[]
flag=0
for i in range(m):
    s = input()
    p.append(list(map(int, s.split(','))))

for i in range(0,len(p)):
    for k in range(0,len(p)):
        if(i==k):continue
        if(p[i][1]==p[k][0]):
            sum.append(k)
            flag=1
            break;
    if (flag==0):
        sum.append(-1)
    flag=0
print(sum)
