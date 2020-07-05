x=int(input())
y=int(input())
bound =int(input())
ans = set()
for i in range(18):
    for j in range(18):
        v = x ** i + y ** j
        if v <= bound:
            ans.add(v)
print(list(ans))