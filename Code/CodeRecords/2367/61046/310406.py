num=int(input())
if num % 2 == 0 or num % 5 == 0:
    ans= -1

r = 0
for k in range(1,num + 1):
    r = (r * 10 + 1) % num
    if r == 0:
        ans=k
        break
print(ans)