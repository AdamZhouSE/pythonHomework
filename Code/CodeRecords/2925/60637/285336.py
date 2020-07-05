n=(int)(input())
enter=input().split(' ')
exit=input().split(' ')
sum=0
for i in range(n):
    if(enter[i]!=exit[i]):
        sum+=1
        enter.remove(exit[i])
        enter.insert(i,exit[i])
print(sum)
