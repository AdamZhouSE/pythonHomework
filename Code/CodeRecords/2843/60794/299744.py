aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
b = [0]*len(a)
b[len(a)-1] = a[len(a)-1]
for i in range(1, len(a)):
    b[len(a)-1-i] = a[len(a)-1-i]
    x = 0
    for j in range(1, i+1):
        if x == 0:
            b[len(a) - 1 - i] = b[len(a)-1-i] + b[len(a)-1-i+j]
            x = 1
        else:
            b[len(a) - 1 - i] = b[len(a) - 1 - i] - b[len(a) - 1 - i + j]
            x = 0
for i in range(len(b)-1):
    print(b[i], "", end="")
print(b[len(b)-1])