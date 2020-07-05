number=int(input())

for i in range(number):
    a = ''
    pstr = input()
    for i in range(len(pstr)-1):
        if pstr[i] != pstr[i+1]:
            a=a+pstr[i]
    if pstr[len(pstr)-1]!=pstr[len(pstr)-2]:
        a = a + pstr[i + 1]
    print(a)