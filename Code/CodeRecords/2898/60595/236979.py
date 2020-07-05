def Test():
    s=int(input())
    binnum=input()
    times=binnum.count("1")
    while(times>1):
        binnum=binnum[:binnum.rfind("1")]+binnum[binnum.rfind("1")+1:]
        times=times-1
    n=len(binnum)
    if(binnum.startswith("0")):
        binnum="1"
        for i in range(1,n):
            binnum=binnum+"0"
    print(binnum,end="")

if __name__ == "__main__":
    Test()
