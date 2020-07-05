def linerlist_7_survive(n,k):
    link = range(1,n+1)
    ind = 0
    for loop_i in range(n-1):
        ind = (ind+k)%len(link)
        ind-=1
        del link[ind]
        if ind==-1:
            ind=0
    print(link[0])
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_7_survive(int(n),1)