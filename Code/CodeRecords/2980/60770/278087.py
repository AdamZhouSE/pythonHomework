def solve():
    src=input()
    ops=input().split()
    op=ops[0]
    p1,p2='',''
    if op=='D':
        p1=ops[1]
    else:
        p1,p2=ops[1:3]

    res=''
    try:
       res = {
           'D': delete(p1,src),
           'I': insert(p1,p2,src),
           'R': rpl(p1,p2,src)
       }[op]
    except BaseException:
        res='no exist\n'+src

    print(res)



def delete(des,src=''):
    pos=src.index(des)
    return src[:pos]+src[pos+1:]

def insert(pos,cnt,src=''):
    sr=src[::-1]
    posi=sr.index(pos)
    posi=len(src)-1-posi
    return src[:posi]+cnt+src[posi:]

def rpl(old,new,src=''):
    return src.replace(old,new)

if  __name__ == '__main__' :
    solve()
