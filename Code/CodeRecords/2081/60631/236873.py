b = input()
a = input()
num = 0
for i in range(len(b)):
    if b[i:len(b)].startswith(a):
        num = num + 1
print(num,end='')