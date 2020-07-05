n = int(input())
max = int((n-1)/2)
res =[]
for i in range(max):
    s="*"*(max-i)+"D"*(2*i+1)+"*"*(max-i)
    res.append(s)
for i in res:
    print(i)
print("D"*n)
for i in reversed(res):
    print(i)