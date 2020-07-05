res = 0
def perm(li, k):
    global res
    # print(li)

    if k == len(li):
        return

    if k > 0:
        if li[k][0]>li[k-1][0] and li[k][1]>li[k-1][1]:
            res = max(res, k)
        else: return

    for i in range(k+1, len(li)):
        li[i], li[k] = li[k], li[i]
        perm(li, k+1)
        li[i], li[k] = li[k], li[i]



if __name__ == '__main__':
    n = int(input())
    li = []
    for i in range(n):
        x = input().strip().split(",")
        li.append([int(x[0]), int(x[1])])
    perm(li, 0)
    if res == 3: print(li)
    print(res+1)