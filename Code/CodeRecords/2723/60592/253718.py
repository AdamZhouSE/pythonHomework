tests = int(input())
for i in range(0,tests):
    ls = input()
    while len(ls)>1:
        res = 0
        for j in range(0,len(ls)):
            res+=int(ls[j])
        ls = str(res)
    print(ls)