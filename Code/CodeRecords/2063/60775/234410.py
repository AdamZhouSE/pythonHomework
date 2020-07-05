a = input()

result = True
for i in range(int((len(a)+1)/2)):
    if a[i] != a[-1 * i -1]:
        result = False
        break
print(result)