def Test():
    s=int(input())
    binnum=input()
    times=binnum.count("1")
    while(times>1):
        binnum=binnum[:binnum.rfind("1")]+binnum[binnum.rfind("1")+1:]
        times=times-1
    print(binnum)

if __name__ == "__main__":
    Test()
