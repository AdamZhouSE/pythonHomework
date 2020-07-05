candies=int(input())
people=int(input())
count=1
res=[0]*people
while(candies>0):
    for i in range(people):
        if count>candies:
            res[i]+=candies
            candies=0
            break
        else:
            res[i]+=count
            candies-=count
            count+=1
print(res)