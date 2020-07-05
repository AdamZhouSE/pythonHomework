x=input().split()
n=int(x[0])
k=int(x[1])
s1=input()
s2=input()
q=int(input())
for I in range(q):
    x=input().split()
    now=s1[int(x[0])-1:int(x[1])]
    tag=s2[int(x[2])-1:int(x[3])]
    num=[i for i in range(int(x[0]),int(x[1])+1)]
    print(now,tag,num)