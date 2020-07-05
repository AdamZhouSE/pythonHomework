aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
list.sort(a)
ans = 0
for i in range(int(len(a)/2)):
    ans = ans + (a[2*i+1]-a[2*i])
print(ans)