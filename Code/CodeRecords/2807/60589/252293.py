nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
num=0
while len(a)>0 and len(b)>0:
    i=a.pop()
    for j in b:
        if (i+j)%2==1:
            num+=1
            b.remove(j)
            break
print(num)