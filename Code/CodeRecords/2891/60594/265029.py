n=(int)(input())
num=[int(n) for n in input().split()]
max=0
for i in num:
    if i>max:
        max=i
total=0
for i in num:
    total+=max-i
print(total)
