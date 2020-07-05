num=int(input())
test=list(input())
count=0
temp=test[0]
for i in range(num-1):
    if temp==test[i+1]:
        count+=1
    temp=test[i+1]
print(count)