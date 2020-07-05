aa = input()
aaa = input().split(" ")
a = []
for i in range(len(aaa)):
    a.append(int(aaa[i]))
odd = 0
even = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(min(odd, even))