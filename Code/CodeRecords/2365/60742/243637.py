# 在长度不足的数字后补0，使所有数字具有相同的长度
# 新数组中同时存入原来的位置，以方便取出原来的元素
t = int(input())
for k in range(t):
    n = int(input())
    a = input().split()
    a_new = []
    length = 0
    for num in a:
        if len(num)>length:
            length = len(num)
    for i in range(len(a)):
        value = list(a[i])
        if len(a[i])!=length:
            for j in range(length-len(a[i])):
                value.append('0')
        a_new.append([i,''.join(value)])
    a_new.sort(key=lambda x:x[1],reverse=True)
    res = []
    for pair in a_new:
        res.append(a[pair[0]])
    print(''.join(res))