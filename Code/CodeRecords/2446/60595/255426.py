def Test():
    n=int(input())
    passages=[]
    for i in range(0,n):
        passages.append(input().split())
    m=int(input())
    for i in range(0,m):
        temp=input()
        result=deal(temp,passages)
        print(" ".join(str(x) for x in result),end=" \n")
def deal(temp,passages):
    result=[]
    for i in range(0,len(passages)):
        if(passages[i].count(temp)!=0):
            result.append(i+1)
    return result
if __name__ == "__main__":
    Test()