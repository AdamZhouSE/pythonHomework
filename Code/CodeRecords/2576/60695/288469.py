a = input()
a = list(map(int, a.split(",")))
target = int(input())
sum = 0
for i in range(0, len(a)):
    sum += a[i]
if sum <= target:
    a = sorted(a)
    print(a[len(a)-1])
else:
    if target/len(a)-target//len(a)==0.5:
        x = target//len(a)
    else:
        x = round(target/len(a))
    print(x)