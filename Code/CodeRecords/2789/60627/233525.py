# 14
inp = input()
n = int(inp)
for i in range(n):
    inp = input()
    inp = input()
    num = inp.split()
    for j in range(len(num)):
        num[j] = int(num[j])
    num.sort(reverse=True)
    for j in range(len(num)):
        if num[j]>=j+1:
            if j == len(num)-1:
                print(j + 1)
                break
            else:
                continue
        else:
            print(j)
            break