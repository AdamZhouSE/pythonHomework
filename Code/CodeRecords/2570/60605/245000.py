res = 0
def perm(li, k):
    global res

    if k == len(li)-1:
        idx = 0
        # print(li)
        while idx < k-1 and li[idx][0] < li[idx+1][0] and li[idx][1] < li[idx+1][1]:
            idx += 1
        res = max(res, idx+1)
        return

    for i in range(k, len(li)):
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
    print(res)