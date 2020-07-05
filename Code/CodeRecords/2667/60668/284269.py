def linerlist_23_how(i,L):
    re = '1'*L
    print(int(re,2)-i+1)
if __name__=='__main__':
    for _ in range(int(input())):
        i,L = input().split()
        linerlist_23_how(int(i),int(L))