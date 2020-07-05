n=bin(int(input()))[2::]
sum=int(n[0])
flag=0
for i in range(1,len(n)-1):
    sum^=int(n[i])
    if sum==0:
        print(False)
        flag=1
        break
    sum=n[i+1]
if flag==0:
    print(True)