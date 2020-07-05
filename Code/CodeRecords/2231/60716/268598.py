import itertools
def findprime(number):
    primelist = list()
    for j in range(2,number):
        check = True
        for k in range(2,j):
            if j%k==0:
                check=False
                break
        if check:
            primelist.append(j)
    return primelist

ucnum = int(input())
ans = list()
for i in range(ucnum):
    number = int(input())
    lists = findprime(number)
    check=False
    for a,b,c in itertools.combinations(lists,3):
        if a*b*c == number:
            check=True
            break
    if check: 
        ans.append(1)
    else:
        ans.append(0)
for i in ans:
    print(i)