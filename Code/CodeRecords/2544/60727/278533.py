def so(l1,l2):
    if l1[1]>l2[1] and l1[3]>l2[3]:
        return 0
    if l1[1]<l2[1] and l1[3]<l2[3]:
        return 0
    if l1[2]<l2[0] or l1[0]>l2[2]:
        return 0
    return 1
num = eval(input())
for i in range(0,num):
    l1=input().split(' ')
    l2=input().split(' ')
    l1 = [int(x) for x in l1]
    l2 = [int(x) for x in l2]
    print(so(l1,l2))