def list(list1):

    one_list = list(list1)

    one_list.sort()

    two_list = []

    n = len(one_list)

    total = sum(one_list)

    half_total = total / 2

    s = 0

    for i in range(n-1, -1, -1):

        ns = s + one_list[i]

        if ns > half_total:

            continue

        else:

            s += one_list[i]

            two_list.append(one_list[i])

            one_list.pop(i)

            if abs(s - half_total) < one_list[0]:

                break
    q=0
    w=0
    for i in range(len(one_list)):
        q+=one_list[i]
    for i in range(len(two_list)):
        w+=two_list[i]
    return abs(q-w)



p=int(input())
for i in range(p):
    m=int(input())
    ls=input().split(' ')
    ls=[int(ls[i]) for i in range(m)]
    x=list(ls)
    print(x)
    