s = input()
t = input()
str = [ s for s in t]

for i in range(1,len(str)):
    for j in range(i):
        if str[i] not in s:
            pass
        elif s.index(str[i]) < s.index(str[j]):
            tmp = str.pop(i)
            str.insert(j,tmp)
            break

for e in str:
    print(e,end='')
print()
