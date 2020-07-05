n=int(input())
name=list(map(str,input().split()))
new=list(map(str,input().split()))
num=0
for i in range(n):
    for j in range(i,n):
        if(new.index(name[i])>new.index(name[j])):
            num+=1
print(num)