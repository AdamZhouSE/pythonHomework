line = input().split(' ')
n = int(line[0])
t = int(line[1])
c = int(line[2])
people = list(map(int,input().split(' ')))
ans1 = ans2 = 0
for i in range(n):
    k = people[i]
    if k>t:
        if ans1>=c:
            ans2+=ans1-c+1
        ans1 = 0
    else:
        ans1 = ans1 + 1
if ans1>=c:
    ans2 += ans1-c+1
print(ans2)