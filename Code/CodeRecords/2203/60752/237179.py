string=input()
for n in range(0,len(string)):
    s=string[0:n]
    for l in range(1,len(string)-n+1):
        smd=0
        if string[0:l]==string[n:n+l]:
            smd=l
            print(1000000007%l)
            continue
    