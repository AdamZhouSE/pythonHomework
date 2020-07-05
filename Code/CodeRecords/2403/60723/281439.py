candies=int(input())
num_people=int(input())
people=[0]*num_people
result=[]
i=1
candies=candies-1
while candies>0:
    result.append(i)
    i=i+1
    candies=candies-i
result.append(candies+i)
for j in range(len(result)):
    people[j%num_people]=people[j%num_people]+result[j]
print(people)