def judge(s,t):
    the_t=list(t)
    #print(the_t)
    l=[]
    for x in s:
        if the_t.count(x)==0:
            return False
        a=the_t.index(x)
        l.append(a)
    k=sorted(l)
    if l==k:
        return True
    else:
        return False
if __name__ == '__main__':
    s=input()
    t=input()
    print(judge(s,t))