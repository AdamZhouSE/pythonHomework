n=int(input())
nodes=input().split()
d=int(input())
max1=2**d-1
begin=2**(d-1)-2
if(max1<len(nodes)):
    for i in range(begin+1,max1-1):
        print(nodes[i],"",end='')
    print(nodes[max1-1])
elif((len(nodes)-1-begin)>0):
    for i in range(begin+1,len(nodes)-1):
        print(nodes[i],"",end='')
    
    print(nodes[len(nodes)-1])
else:
    print("EMPTY")

