def exam10():
    s=list(input())
    t=list(set(s))
    t.sort()
    l=[]
    for i in range(len(t)):
        ind=0
        cou = []
        for j in range(s.count(t[i])):
            cou.append(s.index(t[i],ind)+1)
            ind=s.index(t[i],ind) + 1
            cou.sort(reverse=True)
        l=l+cou
    for i in range(0,len(l)-1):
        print(l[i],end=" ")
    print(l[len(l)-1])
exam10()