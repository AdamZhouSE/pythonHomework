candies = int(input())
num_people = int(input())
people = []

for i in range(num_people):
    people.append(0)

for j in range(num_people):
    now = j+1
    if now <= candies:
        people[j] = people[j] + now
        candies = candies - now
    else:
        people[j] = people[j] + candies
        candies = 0
        break
       
for j in range(num_people):
    now = num_people+j+1
    if now <= candies:
        people[j] = people[j] + now
        candies = candies - now
    else:
        people[j] = people[j] + candies
        candies = 0
        break
        
print(people)        
        