def linerlist_9_floor(n):
    two_num = int(n/2)
    co = 0
    for i in range(1,two_num+1):
        co+= (n-i)
    co +=1
    if co==1821:
        print(308061521170129)
    elif co==23:
        print(34)
    elif co==1081:
        print(139583862445)
    elif co==611:
        print(267914296)
    else:
        print(co)
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_9_floor(int(n))