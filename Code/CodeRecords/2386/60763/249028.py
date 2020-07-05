def del_repeatnum(s):
    s1=[]
    for i in s:
        # print(i)
        is_diff = True
        for j in s1:
            if j == i:
                is_diff = False
                break
        if is_diff:
            s1.append(i)
    return s1

def isSum(s,x):
    l =  map(int, s.split(','))
    if sum(l) == x:
        return True
    else:
        return False

T = int(input())
for i in range(T):
    t_list = []
    N = int(input())
    # list1 = map(int,input().split(' '))
    list1 = input().split(' ')
    x = int(input())
    # print(list1)

    def permutation(s, i):
        if  i == len(s):
            # print(s)
            t_list.append(','.join(s[0:4]))
            # print(t_list)
        else:
            for j in range(i, len(s)):
                s[j], s[i] = s[i], s[j]
                permutation(s, i + 1)
                s[j], s[i] = s[i], s[j]

    permutation(list1,0)
    s1 = del_repeatnum(t_list)
    issum = False
    for i in t_list:
        if isSum(i,x):
            issum = True
            break
    if issum:
        print(1)
    else:
        print(0)