candies = eval(input())
num_people = eval(input())
n = 1
ans = [0]*num_people
index = 0
while candies>0:
    if candies>n:
        ans[index] = ans[index] + n
    else:ans[index] = ans[index] + candies
    index = index + 1
    if index == len(ans):
        index = 0
    candies = candies - n
    n = n + 1
print(ans)