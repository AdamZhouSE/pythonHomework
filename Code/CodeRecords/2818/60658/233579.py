n,x=[int(x) for x in input().split()]
courses=[int(x) for x in input().split()]
courses.sort()
sum=0
for i in courses:
    sum+=(i*x)
    x = x-1 if x > 1 else 1
print(sum)