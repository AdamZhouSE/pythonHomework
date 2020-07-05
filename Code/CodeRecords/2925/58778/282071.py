n=int(input())
intu=list(map(int,input().split( )))
outu=list(map(int,input().split( )))
fine=0
for i in range(n):
    if(intu[-1]!=outu[-1]):
        fine+=1
        x=outu.index(intu[-1])
        del intu[-1]
        del outu[x]
    else:
        del intu[-1]
        del outu[-1]
print(fine)