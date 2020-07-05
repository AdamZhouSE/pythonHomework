def linerlist_24_swap(n):
    n = n[2:]
    co = '1'*len(n)
    re = int(co,2)-int(n,2)
    print(re,end=' ')
    print(int(co,2),end='\n')
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_24_swap(bin(int(n)))