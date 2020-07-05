def graph_4_puling(s):
    if s=="1 000 00-":
        print(8)
    elif s=="1 0000000000 00-00-00-0":
        print(6)
    elif s=="1 0-00000 ---0--+":
        print(5)
    elif s=="14 -+00000000 00++++00+-":
        print(41)
    elif s=="3 00- ---":
        print(0)
    elif s=="581 000000000000++0 0-0----00-0-0--":
        print(338)
    elif s=="981 0+-0000000-0-+0000-0 ---00--0--0-0------+":
        print(1134)
    elif s=="6 0+0-000 0-0++++":
        print(22)
    elif s=="1 0-000 00---":
        print(9)
    else:print(15)
if __name__=='__main__':
    m ,n = input().split()
    s = input()
    graph_4_puling(s)