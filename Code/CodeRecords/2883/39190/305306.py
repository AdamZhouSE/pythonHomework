def func16(n,m):
    fi=fj=0
    li=lj=0
    output=""
    for i in range(n):
        tmp=input()
        for j in range(m):
            if tmp[j]=="B":
                li=i
                lj=j
                if fi==0 and fj==0:
                    fi=i
                    fj=j
    output=str(int((fi+li)/2+1))+" "+str(int((lj+fj)/2+1))
    print(output)
    
ip=input().split(" ")
n=int(ip[0])
m=int(ip[-1])
func16(n,m)