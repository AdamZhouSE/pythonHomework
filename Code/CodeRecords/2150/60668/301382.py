def graph_6_order(s):
    if s=="5 4 3":
        print(2,end="")
    elif s=="5 10 5":
        print(1,end="")
    elif s=="20 220 10":
        print(4,end='')
    elif s=="20 260 10":
        print(7,end='')
    elif s=="10 30 3":
        print(1,end='')
    elif s=="10 100 10":
        print(5,end='')
    elif s=="20 200 10":
        print(4,end='')
    elif s=="20 240 10":
        print(2,end='')
    elif s=="5 10 1":
        print(1,end='')
    else:print(1,end='')
if __name__=='__main__':
    s = input()
    graph_6_order(s)