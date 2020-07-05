k=int(input())
sum=[]
for i in range(k):
    s=input()
    l=list(map(int,s[0:len(s)].split(',')))
    for tmp in l:
        sum.append(tmp)
d=int(input())
sum.sort()
print(sum[d-1])

