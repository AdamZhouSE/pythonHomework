a = input()
b = len(a)
a = a[1:b-1].split(",")
b = len(a)
n = []
for i in a:
    if i!=0:
        x = i
        m = 0
        for j in a:
            if j == x:
                m = m + 1
        if m>b/3 and not(int(i) in n):
                n.append(int(i))
print(n)