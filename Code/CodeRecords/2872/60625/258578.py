n=int(input())
rockList=list(input())
count=0
for index in range(n-1):
    if rockList[index]==rockList[index+1]:
        count+=1
print(count)