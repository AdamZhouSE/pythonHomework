#从英文单词中重建数字
def solve(the_s):
    s=list(the_s)
    """
    e     zero, one, three, five, seven, eight, nine
    f     four, five
    g     eight
    h     three, eight
    i     five, six, eight, nine
    n     one, seven, nine
    o     zero, one, two, four
    r     zero, three, four
    s     six, seven
    t     two, three, eight
    u     four
    v     five, seven
    w     two
    x     six
    z     zero

      """
    t0=s.count('z')
    t2=s.count('w')
    t4=s.count('u')
    t6=s.count('x')
    t8=s.count('g')
    t3=s.count('h')-t8
    t7=s.count('s')-t6
    t5=s.count('v')-t7
    t9=s.count('i')-t5-t6-t8
    t1=s.count('e')-t0-2*t3-t5-2*t7-t8-t9
    w=[]
    w.append(t0)
    w.append(t1)
    w.append(t2)
    w.append(t3)
    w.append(t4)
    w.append(t5)
    w.append(t6)
    w.append(t7)
    w.append(t8)
    w.append(t9)
    re=''
    for i in range(0,10):
        k=w[i]
        p=0
        while p<k:
            re=re+str(i)
            p=p+1
    return re
if __name__ == '__main__':
    m=input()
    print(solve(m))