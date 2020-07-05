def ag(m,n):
    import math
    r=0
    for i in range(int(math.sqrt(m)),int(math.sqrt(n))+(1 if int(math.sqrt(n))!=math.sqrt(n) else 0)):
        if str(i)==str(i)[::-1] and str(i*i)==str(i*i)[::-1]:
            r+=1
    print(r)
if __name__ == '__main__':
    ag(int(input()),int(input()))
