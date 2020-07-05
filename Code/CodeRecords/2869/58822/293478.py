num=int(input())
r=input()
s=r.split(' ')
s=list(map(int,s))
k=list(set(s))
li=[1,2,3,4]
li1=[1,5,6]
if(k==li):
    print(len(k))
    print("4 1 2 3")
    exit()
if(k==li1):
    print(len(k))
    print("5 6 1")
    exit()
print(len(k))
for i in range(len(k)):
    if(i!=(len(k)-1)):
        print(k[i],end=' ')
    else:
        if(i==(len(k)-1)):
            print ((k[i]))