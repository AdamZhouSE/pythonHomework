nums = input()
tmp = nums[2:len(nums) - 2].split('],[')
restaurants = [[] for i in range(len(tmp))]
for i in range(len(tmp)):
    num = tmp[i].split(',')
    for j in range(len(num)):
        restaurants[i].append(int(num[j]))
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())

for rest in restaurants:
    if veganFriendly and not rest[2]:
        rest[1] = 0
    elif maxPrice < rest[3] or maxDistance < rest[4]:
        rest[1] = 0
restaurants.sort(key=lambda x: [x[1], x[0]], reverse=True)

res = '['
for rest in restaurants:
    if rest[1]:
        res += str(rest[0]) + ', '
res = res[:len(res) - 2] + ']'
print(res)
