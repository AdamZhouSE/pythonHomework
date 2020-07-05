a = input()
b = input()
a = a[1:len(a)-1].split(",")
c = -1
for i in range(len(a)):
    if a[i] == b:
        c = i
        break
print(c)