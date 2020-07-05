def get_area(li):
    ul = []
    size = len(li)
    for i in range(size):
        curr = li[i]
        left = right = i
        for j in range(left, -1, -1):
            if li[j] >= curr:
                left = j
            else:
                break
        for k in range(right, size, 1):
            if li[k] >= curr:
                right = k
            else:
                break
        area_new = curr * (right - left + 1)
        u_new = [left, right, li[i], area_new]
        if len(ul) == 0:
            ul.append(u_new)
        else:
            u = ul[0]
            area_old = u[2] * (u[1] - u[0] + 1)
            if area_old < area_new:
                ul = [u_new]
            elif area_old == area_new:
                ul.append(u_new)
    return ul


num = int(input())
for n in range(num):
    long=int(input())
    numListStr=input().split()
    numList = []
    for element in numListStr:
        numList.append(int(element))
    res=get_area(numList)
    res=res[0]
    print(res[3])