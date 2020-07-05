num=int(input())
mm=num
test=input().split()
test=list(map(int, test))
com=sorted(test)
com.reverse()
ans=0
while num>0:
    if test==com:
        ans+=1
        temp=test.pop()
        
        test.insert(0,temp)
    num-=1
if 0<ans<=mm:
    print(ans)
else:
    print(-1)