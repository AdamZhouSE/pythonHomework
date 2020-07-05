a=int(input())
n=list(map(int,input().split()))
sub=[]
count=0
before=0
for i in range(a):
    if n[i]>before:
        count+=1
    else:
        sub.append(count)
        count=1
    before = n[i]
sub.append(count)
print(max(sub))