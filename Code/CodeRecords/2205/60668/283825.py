def linerlist_11_handshake(n):
    su = 0
    if n==0:
        su = 1
    for i in range(n):
        j = n-1-i
        su = su + linerlist_11_handshake(i)*linerlist_11_handshake(j)
    return su
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        print(linerlist_11_handshake(int(int(n)/2)))