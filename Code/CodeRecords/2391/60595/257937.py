def Test():
    n=int(input())
    names=[]
    has=[]
    for i in range(0,n):
        names.append(input())
        has.append(0)
    m=int(input())
    for i in range(0,m):
        s=input()
        try:
            j=names.index(s)
            if(has[j]==0):
                print("OK")
                has[j]=1
            else:
                print("REPEAT")
        except:
            print("WRONG")
if __name__ == "__main__":
    Test()