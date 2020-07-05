N = int(input())
result = []
while N > 0:
    this = "Yes"
    x = input()
    y = input()
    if x == y:
        this = "Yes"
    else:
        if len(x) == len(y) == 1:
            this = "No"
        else:
            this = "No"
            # 看x是不是y前面的连续子字符串
            for i in range(1, len(y) + 1):
                t = y[:i]
                if x == t:
                    this = "Yes"
                    break
            if this != "Yes":
                this = "Yes"
                # 从后面开始看
                i = len(x) - 1
                j = len(y) - 1
                while i >= 0:
                    nx = x[i]
                    ny = y[j]
                    if y[j] != x[i]:
                        r = j
                        vx = x[i]
                        vy = y[j]
                        while y[j] != x[i]:
                            j = j - 1
                            if j == 0:
                                this = "No"
                                break
                        l = j + 1
                        sub = y[j + 1:r + 1]
                        if sub[0] == x[i]:
                            this = "No"
                        for k in range(len(sub) - 1):
                            if sub[k] == sub[k - 1]:
                                this = "No"
                                break
                        i = i - 1
                        j = j - 1
                    else:
                        i = i - 1
                        j = j - 1
                    if j == 0 or this == "No":
                        break
            # 看X是不是Y后面的子字符串
            if this == "Yes":
                i = len(y) - 1
                while i >= 0:
                    t = y[i:]
                    if x == t:
                        t = y[:i]
                        if t[len(t) - 1] == y[i]:
                            this = "No"
                        for i in range(len(t) - 1):
                            if t[i] == t[i + 1]:
                                this = "No"
                                break
                        zzz=False
                        for i in range(len(t)):
                            if t[i]==x[0]:
                                zzz=True
                                break
                        if not zzz:
                            this="No"
                    if this == "No":
                        break
                    else:
                        i = i - 1
            if len(y) < len(x):
                this = "No"

    result.append(this)
    N = N - 1

for i in range(len(result)):
    print(result[i])