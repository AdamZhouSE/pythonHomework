n=input().split(',')
n=[int(i) for i in n]
k=int(input())
cons=[]
for i in range(len(n)-1):
    new=[n[i]]
    for m in range(i+1,len(n)):
        new.append(n[m])
    if(sum(new)%k==0):
        mark=0
        break
    else:
        mark=1

if(mark==1):
    print("False")
else:
    print("True")