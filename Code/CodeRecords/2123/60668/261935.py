def nums_15_validNum(n):
    co = False
    for i in range(n):
        if n%i==0 and n/i==i:
            co = True
    print(co)
if __name__=='__main__':
    n = int(input())
    nums_15_validNum(n)