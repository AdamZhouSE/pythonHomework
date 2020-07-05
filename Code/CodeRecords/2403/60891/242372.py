candies = int(input())
num_people = int(input())
ans = []

for i in range(num_people):
    ans.append(0)

candies_num = candies
give_num = 0
while candies_num > 0:
    if candies_num > give_num:
        give_num += 1
        ans[(give_num % num_people) - 1] += give_num
    else:
        index = give_num % num_people
        give_num = candies_num
        ans[index] += give_num
    candies_num -= give_num
print(ans)
