a=eval(input())
for i in range(a):
    t=[]
    s1=input()
    s2=input()
    s1=set([x for x in s1])
    s2=set([x for x in s2])
    t=list(s1.union(s2)-s1.intersection(s2))
    t.sort()
    st=""
    for i in t:
        st+=i
    print(st,end="\n\n")