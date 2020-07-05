num=list(map(int,input().strip().split(",")))
sorted(num)
result=max(num[0]*num[1]*num[-1], num[-1]*num[-2]*num[-3])
print(result)