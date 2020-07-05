def minBin():
    N=int(input())
    bi=input()
    Ones=0
    for num in bi[1:]:
        if num=='1':
            Ones+=1
    res="1"
    for i in range(0,len(bi)-1-Ones):
        res+="0"
    print(res)

if __name__=='__main__':
    minBin()