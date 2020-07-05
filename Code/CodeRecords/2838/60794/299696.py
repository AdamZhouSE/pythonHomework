aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
list.sort(a)
ans = 0
for i in range(int(len(a)/2)):
    ans = ans + (a[i] + a[len(a)-1-i])*(a[i] + a[len(a)-1-i])
print(ans)