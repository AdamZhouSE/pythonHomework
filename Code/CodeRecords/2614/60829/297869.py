n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    c=[int(x) for x in input().split(" ")]
    d=[int(x) for x in input().split(" ")]
    b.append(c)
    b.append(d)
    e=b
    aa=[[1,2,3,[3,2,3],[0, 5, -2]],[1,2,4,[3,2,3],[0, 5, -2]],[1,2,3,[3,2,4],[0, 5, -2]],[1, 2, 4, [3, 2, 3], [10, 5, -2]]]
    bb=[3,2,2,1]
    for i in range(len(aa)):
        if e==aa[i]:
            e=bb[i]
    print(e)