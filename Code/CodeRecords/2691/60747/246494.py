n=int(input())
result=[]
for i in range(n):
    a=int(input())
    list1=input().split(" ")
    for j in range(a):
        list1[j]=int(list1[j])
    one_list = list(list1)
    one_list.sort()
    two_list = []
    m = len(one_list)
    total = sum(one_list)
    half_total = total / 2
    s = 0
    for i in range(m-1, -1, -1):
        ns = s + one_list[i]
        if ns > half_total: continue
        else:
            s += one_list[i]
            two_list.append(one_list[i])
            one_list.pop(i)
            if abs(s - half_total) < one_list[0]:
                break
    one=0
    two=0
    for j in one_list:
        one = one +j
    for k in two_list:
        two = two + k
    if one>two:result.append(one-two)
    else:result.append(two-one)
for f in range(n):
    print(result[f])