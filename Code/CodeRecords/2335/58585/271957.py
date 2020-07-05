X=int(input())
Y=int(input())
count=0
while(X<Y):
    if X<=int(Y/2):
        X*=2
        count+=1
    else:
        break
if X<Y:
    count+=X-int(Y/2)+1
    print(count)
else:
    print(count+X-Y)