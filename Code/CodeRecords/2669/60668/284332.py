def linerlist_25_son(n):
    co = []
    for i in range(n,0,-1):
        if i & n == i:
            co.append(i)
    for item in co:
        print(item ,end=' ')
    print(0,end=' \n')
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_25_son(int(n))