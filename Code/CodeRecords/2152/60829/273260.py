a= int(input())
orzfangs = [int(i) for i in input().split(' ')]
temp = [int(i)-1 for i in input().split(' ')]
for i in range(a):
    res = 0
    label = [True for j in range(a)]
    while label[i]:
        res += orzfangs[i]
        label[i] = False
        i = temp[i]
    print(res)