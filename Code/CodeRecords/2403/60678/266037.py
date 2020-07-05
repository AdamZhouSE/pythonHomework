candies = int(input())
num_people = int(input())
get_candies = [0] * num_people
shouldGet = 1
while candies > 0:
    for i in range(0, num_people):
        if candies <= shouldGet:
            get_candies[i] += candies
            candies = 0
            break
        get_candies[i] += shouldGet
        candies -= shouldGet
        shouldGet += 1
print(get_candies)