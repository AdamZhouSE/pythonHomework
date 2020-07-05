def candiesDistribution(candies, num_people):
    ans = [0 for _ in range(num_people)]
    counter = 0
    while candies > counter:
        ans[counter % num_people] += counter + 1
        counter += 1
        candies -= counter
    ans[counter % num_people] += candies
    return ans

candies = int(input())
num_people = int(input())
print(candiesDistribution(candies, num_people))
