def f(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic


def is_in(d,s):
    dic={}
    for i in s:
        if i in d:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
    return dic==d                

T = int(input())
for sample in range(T):
    s1 = input()
    s = input()
    d = f(s)
    length = len(s)
    ans=False
    while length <= len(s1):

        for i in range(0, len(s1) - length + 1):
            subs = s1[i:i + length + 1]
            if is_in(d, subs):
                print(subs)
                ans=True
                break
        if ans:
            break
        length += 1
    if not ans:
        print(-1)
        print()
