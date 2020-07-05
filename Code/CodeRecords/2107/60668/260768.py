def nums_10_numTwo(n):
    co = False
    for i in range(0,n):
        if pow(i,2)>n:
            break
        elif pow(i,2)==n:
            co = True
            break
    print(co)
if __name__=='__main__':
    n = int(input())
    nums_10_numTwo(n)