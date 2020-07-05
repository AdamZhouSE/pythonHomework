candies = int(input())
num_people = int(input())
i = 0
res = [0]*num_people
while(candies>0):
    if candies>=i+1:
        candies-=i+1
        res[i%num_people] += i+1;
    else:
        res[i%num_people] += candies
        candies = 0;
    i = i+1
print(res)