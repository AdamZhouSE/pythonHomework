def fac(x):
    if x==1 or x==0:return 1
    return x*fac(x-1)

n = int(input())
k = int(input())
li = list(range(n+1))
cur = n-1
ans = ""
while k>0:
    temp = fac(cur)
    index = k//temp+(k%temp)%2
    k = k-temp
    ans = ans + str(li.pop(index))
    cur -= 1
while len(li)>1:
    ans += str(li.pop(1))
print(ans)