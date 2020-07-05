n = input()
maxi = sorted(list(n))
maxi.reverse()
maxi = int(''.join(maxi))
base = [1]
i = 1
while base[-1] < maxi:
    base.append(int(pow(2, i)))
    i += 1
find = False
for i in base:
    if sorted(str(i)) == sorted(n):
        find = True
        break
print(find)
