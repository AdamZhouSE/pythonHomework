import functools,collections
# t=int(input())
# for i in range(t):
#     n=int(input())
#     p=[]
#     l = eval('[' + input().replace(' ', ',') + ']')
#     for j in l:
#         if j%3==0:
#             p.append(j)
# def add(a,b):
#     return a+b
# aver=functools.reduce(add,l)/len(l)
# l = eval('[' + input().replace(' ', ',') + ']')
def maxLength(arr) -> int:
    res = [[]]

    for e in arr:
        if len(set(list(e))) < len(e):  # 自身有重复
            continue
        lens = len(res)
        for i in range(lens):

            if not set(list(''.join(res[i]))) & set(list(e)):  # 添加且与之前的不重复
                res.append(res[i] + [e])
    return max([len(''.join(i)) for i in res])  # 选出最长
print(maxLength(eval(input())))
# m=collections.Counter(n)
