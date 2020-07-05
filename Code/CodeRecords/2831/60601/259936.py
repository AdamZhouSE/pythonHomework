n = eval(input())
station = list(map(int,input().split(' ')))
sum = 0
for i in station:
    sum += i
line = input().split(' ')
s = int(line[0])
t = int(line[1])
load = 0
if s>t:#保证s<t
    s,t = t,s
for i in range(s-1,t-1):
    load = load + station[i]
load = min(load,sum-load)
print(load)