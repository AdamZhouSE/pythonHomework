n=bin(int(input()))[2::]
sum=0
flag=0
for i in range(0,len(n)-1):
    sum=int(n[i])^int(n[i+1])
    if sum==0:
        print(False)
        flag=1
        break
if flag==0:
    print(True)