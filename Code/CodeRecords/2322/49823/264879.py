def ag(m,n):
    import math
    r=0
    for i in range(m,n+1):
        if int(math.sqrt(i))==math.sqrt(i) and str(i)==str(i)[::-1] and str(int(math.sqrt(i)))==str(int(math.sqrt(i)))[::-1]:
            r+=1
    print(r)

if __name__ == '__main__':
    ag(int(input()),int(input()))
