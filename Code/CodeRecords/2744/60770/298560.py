def solve():
    n=int(input())
    sts=[]
    for i in range(n):
        sts.append(input()[2:])
    res=0
    for i in range(n):
        for j in range(n):
            if cmbIsOk(sts[i],sts[j]):
                res+=1
    print(res)
    
def cmbIsOk(s1,s2):
    s=s1+s2
    if s[::-1]==s:
        return True
    return False

if __name__ == '__main__':
    solve()

