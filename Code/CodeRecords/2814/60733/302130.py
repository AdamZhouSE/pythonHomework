n,t = input(),sorted(map(int,input().split()))
sum = 0
a = 0
for p in t:
    if p >= sum:
        a+=1
        sum +=p
print(a)