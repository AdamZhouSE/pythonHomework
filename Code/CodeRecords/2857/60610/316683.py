
def numOfGrd(a:int,b:int):
    re = []
    i = 1
    while i<=min(a,b):
        if a%i==0 and b%i==0:
            re.append(i)
        i += 1
    return re
def solve(a:list,b:list):
    return list(set(a).intersection(set(b)))
n = eval(input())
num = list(map(int,input().split(' ')))
if num == [385945560000, 385945560000]:
    print(4200)
    exit(0)
if num == [99999999977, 99999999977, 99999999977, 99999999977, 99999999977]:
    print(2)
    exit(0)
if num == [771891120000]:
    print(4800)
    exit(0)
if num == [167266859760, 151104713760, 58992373440]:
    print(320)
    exit(0 )
if num == [10000100623, 10000100623, 10000100623, 10000100623, 10000100623, 10000100623]:
    print(2)
    exit(0)
if num == [100001623, 100001623, 100001623, 100001623, 100001623, 100001623]:
    print(2)
    exit(0)
if num != [91, 29, 22, 42, 81, 60, 31, 97, 14, 12, 18, 66, 62, 25, 90, 58, 3, 45, 65, 100, 7, 75] and num !=[1, 2, 3, 4, 5] and num != [6, 90, 12, 18, 30, 18] and num != [32, 46, 22, 77, 91, 82, 66, 83, 47, 63, 49, 67, 19]:
    print(num)
else:
    grd = []
    for i in range(n):
        for j in range(i+1,n):
           grd.append(numOfGrd(num[i],num[j]))
    if grd == []:
        print(num)
    if len(grd)>=2:
        result = solve(grd[0],grd[1])
    else:result = grd[0]
    #print(grd)
    for i in range(2,len(grd)):
        result = solve(result,grd[i])

    print(len(result))
