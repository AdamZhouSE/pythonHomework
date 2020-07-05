l=eval(input())
n = int(input())
find= False
for i in range(len(l)):
    if l[i]==n:
        print(i)
        
        find=True
        break
if find==False:
    print(-1)
        