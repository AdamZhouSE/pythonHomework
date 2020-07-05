candies = int(input())
num_people =int(input())
ans = [0 for i in range(num_people)]
target = 1
index = 0
while(candies>0):
    if(candies >= target):
        ans[(target-1)%num_people] += target
        candies -= target
    else:
        ans[(target-1)%num_people] += candies
        candies = 0
    target +=1
print(ans)
