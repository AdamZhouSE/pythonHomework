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

def same(s,s1):
    count = 0
    for i in range(len(s)-len(s1)+1):
        if s[i:i+len(s1)] == s1:
            count +=1
    return count

T = int(input())
for i in range(T):
    t_list =[]
    def permutation(s, i):
        if i == len(s):
            # print(s)
            t_list.append(''.join(s))
            # print(t_list)
        else:
            for j in range(i, len(s)):
                s[j], s[i] = s[i], s[j]
                permutation(s, i + 1)
                s[j], s[i] = s[i], s[j]

    s = input()
    t = list(input())
    permutation(t,0)
    #print(del_repeatnum(t_list))
    s1 = del_repeatnum(t_list)
    count = 0
    for i in s1:
        #print(same(s,str(i)))
        count += same(s,str(i))
    print(count)