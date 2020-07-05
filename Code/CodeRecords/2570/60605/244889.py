res = 0
def perm(li, k):
    global res
    # print(li)
    if k>1:
        if k > 1 and li[k-1][0] > li[k-2][0] and li[k-1][1] > li[k-2][1]:
            res = max(res, k)
        else:
            return

    if k == len(li):
        return

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
    # if (res+1==3):print(li)
    print(res+1)