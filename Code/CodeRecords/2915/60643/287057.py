if __name__=="__main__":
    n=int(input())
    data=input().split()#[1,2,4,8]#
    data=[int(x) for x in data]
    maxN=1
    temp=1
    for i in range(len(data)-1):
        if data[i+1]<=2*data[i]:
            temp+=1
        else:
            maxN=max(maxN,temp)
            temp=1
        maxN = max(maxN, temp)
    print(maxN)