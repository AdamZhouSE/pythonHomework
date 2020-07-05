n=int(input())
a=int(input())
b=int(input())
count=0
index=1
while(True):
    if(index%a==0 or index%b==0):
        count+=1
    if(count==n):
        break
    index+=1
print(index)

