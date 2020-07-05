def bm(n):
    if n%2==0 or n%5==0:
        print(-1)
    else:
        r=1
        while True:
            if int('1'*r)%n==0:
                print(r)
                return
            r+=1
if __name__ == '__main__':
    bm(int(input()))
