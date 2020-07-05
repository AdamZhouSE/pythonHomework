def minBin():
    N=int(input())
    bi=input()
    Zeros=0
    for num in bi[1:]:
        if num=='0':
            Zeros+=1
    res="1"
    for i in range(0,Zeros):
        res+="0"
    print(res)

if __name__=='__main__':
    minBin()