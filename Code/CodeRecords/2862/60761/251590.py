n=int(input())
numlist=list(map(int,input().split(" ")))
evens=[]
odds=[]
for i in numlist:
    if (i%2==0):
        evens.append(i)
    else:
        odds.append(i)
evens.sort()
odds.sort()
if(len(evens)>len(odds)):
    print(sum(evens[:len(evens)-len(odds)-1]))
elif(len(evens)<len(odds)):
    print(sum(odds[:len(odds)-len(evens)-1]))
else:
    print(0)