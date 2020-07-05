number=int(input())

for i in range(number):
    check=1
    a = ''
    pstr = input()
    for i in range(len(pstr)):
        if pstr[i] not in a:
            a = a + pstr[i]
        else:
            check=0
            break
    print(check)