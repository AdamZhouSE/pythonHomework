num=int(input())
test=input().split()
test=list(map(int,test))
test=sorted(test)
res=0
i=0
while (i<num-1):
    res+=test[i+1]-test[i]
    i+=2
print(res)