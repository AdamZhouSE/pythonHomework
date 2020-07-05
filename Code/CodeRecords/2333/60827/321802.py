x = int(input())
y = int(input())
bound = int(input())
imax,jmax= 0,0
while x**imax<bound:
    imax+=1
while y**jmax<bound:
    jmax+=1
ans = set()
for i in range(imax):
    for j in range(jmax):
        temp = x**i+y**j
        if temp<=bound:
            ans.add(temp)
ans = list(ans)
ans.sort()
print(ans)