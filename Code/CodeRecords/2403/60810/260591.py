candies = int(input())
num_people = int(input())

res = [0] * num_people
i = 0

while candies > i:
    res[i % num_people] += (i+1)
    candies -= (i+1)
    i += 1
res[i % num_people] += candies
print(res)