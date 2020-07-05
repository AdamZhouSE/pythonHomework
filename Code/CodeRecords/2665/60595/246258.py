def Test():
    s=input().split()
    lohia=int(s[0])
    gosu=int(s[1])
    A=0
    B=0
    prince=int(s[2])
    while(prince>1):
        if(lohia%prince==0):
            A=A+1
            lohia=lohia-1
        if(gosu%prince==0):
            B=B+1
            gosu=gosu-1
        prince=prince-1
    prince(str(A)+" "+str(B))

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()