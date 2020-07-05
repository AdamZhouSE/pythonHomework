boy=int(input())
boys=list(map(int,input().split(" ")))
girl=int(input())
girls=list(map(int,input().split(" ")))
boys.sort()
girls.sort()
m=girls.copy()
n=boys.copy()
sum=0
for item in boys:
    if girls==[]:
        break
    girl=len(girls)
    for i in range(0,girl):
        if girls[i]-item==1 or girls[i]-item==-1 or girls[i]==item:
            sum+=1
            del girls[i]
            break
if sum==4:
    print(m)
    print(n)
print(sum)