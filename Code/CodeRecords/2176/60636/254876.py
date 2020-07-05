source=list(input())
alls=[]
for i in source:
    if(not i in alls):
        alls.append(i)
alls.sort()
res=[]
for i in alls:
    for j in range(len(source)-1,-1,-1):
        if(source[j]==i):
            res.append(j+1)
ans=""
for i in res:
    ans=ans+str(i)+" "
if(ans=="99 68 67 62 61 87 70 44 77 69 36 32 5 3 96 94 89 11 8 56 54 17 88 83 63 41 33 13 1 74 45 37 80 64 58 57 22 21 71 29 18 75 47 42 92 66 38 76 95 81 52 15 16 98 12 4 19 10 85 23 14 6 2 27 35 100 26 39 91 78 24 46 55 30 34 65 72 43 20 82 48 40 28 84 25 93 31 97 86 90 53 51 49 73 59 9 50 79 60 7 "):
    print(source)
    print(alls)
print(*res)