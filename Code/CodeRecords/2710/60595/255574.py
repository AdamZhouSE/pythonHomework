
def Test():
    n,k=map(int,input().split())
    d={}
    for i in range(k):
        s=input().split()
        if(s[0]=="M"):
            d[int(s[1])]=int(s[2])
        elif(s[0]=="D"):
            year=int(s[2])
            station=int(s[1])
            print(deal(year,station,d))
def deal(year,station,d):
    result=[]
    for x in d:
        if(station>=x and d[x]>=year):
            result.append(d[x])
    return min(result) if result else -1
if __name__ == "__main__":
    Test()