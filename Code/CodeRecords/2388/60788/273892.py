a=int(input().strip())
for i in range(a):
    length=int(input().strip())
    s=[int(x) for x in input().strip().split()]
    t=[int(x) for x in input().strip().split()]
    flag=True
    for ele in s:
        if s.count(ele)!=t.count(ele):
            print('0')
            flag=False
            break
    if flag:
        print('1')
            