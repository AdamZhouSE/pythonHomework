n = int(input())
a = input().split(" ")
a = [int(x) for x in a]
# 下面删除数组中有倍数关系的：
i = 0
while i < len(a) - 1:
    j = i + 1
    while j < len(a):
        if a[j] % a[i] == 0:
            del a[j]
            j = j - 1
        elif a[i] % a[j] == 0:
            del a[i]
            i = i - 1
            break
        j = j + 1
    i = i + 1
if len(a) == 1:
    if a[0] == 1 :
        print(1)
    elif a[0]==2 or a[0]==3 or a[0] % 6 == 1 or a[0] % 6 == 5:
        print(2)
    else:
        result = 0
        i = 1
        while i * i < a[0]:
            if a[0] % i == 0:
                result = result + 2
            i = i + 1
        if a[0] / i == i:
            result = result + 1
        print(result)

else:
    ma = max(a)
    mi = min(a)
    keneng = []
    if mi == 1:
        print(1)
    else:
        if mi == 2 or mi == 3 or mi%6==1 or mi%6==5:
            keneng.append(1)
            keneng.append(mi)
        else:
            i = 1
            while i * i < mi:
                if mi % i == 0:
                    keneng.append(i)
                    keneng.append(mi / i)
                i = i + 1
            if mi % i == i:
                keneng.append(i)
        for i in range(len(a)):
            if a[i] > mi:
                j = 0
                while j < len(keneng):
                    if a[i] % keneng[j] != 0:
                        del keneng[j]
                    else:
                        j = j + 1
        print(len(keneng))

