a = input()
isEcho = True
for i in range(int(len(a)/2)):
    if a[i] != a[len(a)-i-1]:
        isEcho = False
        break
print(isEcho)