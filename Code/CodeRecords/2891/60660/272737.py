t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
l.sort()
m=l[-1]
result=0
for i in range(t):
    result+=m-l[i]
print(result)