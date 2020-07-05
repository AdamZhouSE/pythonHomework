n=int(input())
num=[int(n) for n in input().split()]
num.sort()
zancun=num.copy()
muqian=num[n-1]
cz=muqian
num.remove(muqian)
duishu=1
while len(num)!=0:
    if cz==0:
        duishu+=1
        muqian=num[len(num)-1]
        cz=muqian
        num.remove(muqian)
    else:
        cunzai=False
        cunzai2=False
        cunzai3=False
        for index in range(len(num)):
            if num[len(num) - 1 - index] == cz-1:
                muqian = num[len(num) - 1 - index]
                cunzai = True
                cunzai2=True
                cunzai3=True
                break
        if not cunzai:
            for index in range(len(num)):
                if num[len(num) - 1 - index] == cz:
                    muqian = num[len(num) - 1 - index]
                    cunzai2 = True
                    cunzai3=True
                    break
        if not cunzai2:
            for index in range(len(num)):
                if num[len(num) - 1 - index] < cz - 1:
                    muqian = num[len(num) - 1 - index]
                    cunzai3=True
                    break
        if not cunzai3:
            muqian=num[0]
        cz = min(muqian, cz - 1)
        num.remove(muqian)
print(duishu)
