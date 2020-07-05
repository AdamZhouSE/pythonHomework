candies = int(input())
num_people=int(input())
ans=[]
for num in range(1,num_people+1):
    if candies>=num:
        ans.append(num)
        candies = candies - num
    else:
        ans.append(candies)
        candies=0

if candies>0:
    ans[0]=ans[0]+candies
print(ans)