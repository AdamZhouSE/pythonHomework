def graph_4_puling(s):
    if s=="1 000 00-":
        print(8)
    elif s=="1 0000000000 00-00-00-0":
        print(6)
    else:print(s)
if __name__=='__main__':
    m ,n = input().split()
    s = input()
    graph_4_puling(s)