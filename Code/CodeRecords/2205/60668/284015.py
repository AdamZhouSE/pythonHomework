def linerlist_11_handshake(n):
    su = 0
    if n==0:
        su = 1
    if n%2==0:
        for i in range(int(n/2)):
            j = n-i-1
            su = su + linerlist_11_handshake(i)*linerlist_11_handshake(j)*2
    else:
        for i in range(int((n-1)/2)):
            j = n-1-i
            su = su + linerlist_11_handshake(i)*linerlist_11_handshake(j)*2
        su += linerlist_11_handshake(int((n-1)/2))*linerlist_11_handshake(int((n-1)/2))
    return su
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        print(linerlist_11_handshake(int(int(n)/2)))