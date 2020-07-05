l = eval(input())

re = []
for i in range(len(l)):
    if i == len(l)-1:
        re.append(0)
        break
    n = 0
    for j in range(i+1,len(l)):
        if l[j] < l[i]:
            n += 1
    re.append(n)
print(re)