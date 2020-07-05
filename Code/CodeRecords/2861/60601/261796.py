n = eval(input())
people = list(map(int,input().split(' ')))
people.sort()
T = 0
for i in range(0,n-1,2):
    if people[i] == people[i+1]:
        continue
    else:
        T = T + people[i+1]-people[i]
print(T)