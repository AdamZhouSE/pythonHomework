n = eval(input())
gift = list(map(int,input().split(' ')))
people = [0]*n
for i in range(len(gift)):
    people[gift[i]-1] = i + 1
print(' '.join(map(str,people)))