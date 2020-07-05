num=int(input().strip())
for i in range(num):
    line1=input().strip()
    line2=input().strip()
    length=int(line1.split()[1])
    s=[int(x) for x in line2.split()]
    s.sort(reverse=True)
    for k in range(length):
        print(s[k],end=' ')
    print("")