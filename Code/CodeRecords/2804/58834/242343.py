numbers=input()
m=numbers.split('+')
lenth=len(m)
for number in range(0,lenth):
    for d in range(number+1,lenth):
        if int(m[number]) > int(m[d]):
            i = m[number]
            m[number] = m[d]
            m[d] = i
    else:
        continue
for number in range(0,lenth-1):
    print(m[number]+'+',end='')
print(m[lenth-1])