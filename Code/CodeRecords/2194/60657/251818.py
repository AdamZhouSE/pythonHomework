num=int(input())
a=input().split(' ')
b=input().split(' ')



def find(a,b):
    cons=[]
    count=0
    for i in range(a,b+1):
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
        if count < 3 and i!=1:
            cons.append(i)
        count = 0
    return cons
cons1=find(int(a[0]),int(a[1]))
cons2=find(int(b[0]),int(b[1]))
cons1=[str(x) for x in cons1]
cons2=[str(x) for x in cons2]
print(' '.join(cons1))
print(' '.join(cons2))