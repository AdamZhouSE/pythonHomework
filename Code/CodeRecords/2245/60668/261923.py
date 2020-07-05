def nums_13_Two(n):
    n_t = bin(n)
    co = 0
    for i in range(2,len(n_t)):
        if n_t[i]=='1':
            for j in range(i+1,len(n_t)):
                if n_t[j]=='1':
                    co = max(co,j-i)
                    break
    print(co)
if __name__=='__main__':
    n = int(input())
    nums_13_Two(n)