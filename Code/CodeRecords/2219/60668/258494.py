def nums_3_plus(n):
    co = False
    for i in range(1,n):
        for j in range(i,n):
            if i*i+j*j==n:
                co=True
    print(co)
if __name__=='__main__':
    n = int(input())
    nums_3_plus(n)