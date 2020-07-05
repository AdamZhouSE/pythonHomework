res = 0
def perm(li, k):
    global res
    # print("Ori", str(k), li)

    if k == len(li):
        return

    if k > 0:
        # 从0监测到k:
        isOK = True
        for i in range(k):
            if li[i][0]>=li[i+1][0] and  li[i][1]>=li[i+1][1]:
                isOK = False
                break
        if isOK:
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
    print(res)