def func():
    temp_arr = [int(x) for x in input().split(" ")]
    n = temp_arr[0]
    r = temp_arr[1]
    avg = temp_arr[2]

    ab = [] * n
    i = 0
    while i < n:
        a, b = input().split(" ")
        ab.append((int(a), int(b)))
        i += 1

    ab.sort(key=lambda x: x[1])

    sum_ab_1 = 0
    for ele in ab:
        sum_ab_1 += ele[0]
    if sum_ab_1 >= avg * n:
        print(0)
        return

    papers = 0
    point_needed = avg * n - sum_ab_1
    i = 0
    while i < n:
        capability = r - ab[i][0]  # 还能窜几分
        if capability >= point_needed:
            papers += point_needed * ab[i][1]
            point_needed = 0
            print(papers)
            return
        else:
            point_needed -= capability
            papers += capability * ab[i][1]
        i += 1


func()
