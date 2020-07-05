n=0
N=int(input())
exist=[]
S=input().split(' ')
for i in S:
    if i in exist:
        exist.remove(i)
    else:
        exist.append(i)
        if(len(exist)>n):
            n+=1;
print(n)
        
    