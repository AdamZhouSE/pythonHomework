rb=input()
stones=input()
count=0
for i in range(len(stones)-1):
    if(stones[i]==stones[i+1]):
        count+=1
print(count)