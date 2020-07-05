num = int(input())
temp = list(input().split(" "))
lists = []

for x in temp:
    lists.append(int(x))


def judge(k, lists):
    if k == len(lists) - 1:
        slide=lists[0:3]
        if sum(slide)-max(slide) > max(slide):
            return True
        else:
            return False
    else:
        res = False
        for i in range(k, len(lists)):
            x = lists[i]
            lists[i] = lists[k]
            lists[k] = x
            res = res or judge(k + 1, lists)
        return res


result = judge(0, lists)
if result:
    print("YES")
else:
    print("NO")
