def au(l):
    r=0
    for i in range(len(l)):
        r+=1 if au_1(l,0,i,len(l)-1) else 0
    print(r+1)
def au_1(l,m,k,n):
    for i in range(m,n+1):
        if (l[i]-l[k])*(i-k)<0:
            return False
    return True
if __name__ == '__main__':
    au(eval(input()))
