def iszhi(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True
def notin(m,list):
    for item in list:
        if m==item:
            return True
    return False
def find(k,list):
    result=[1]
    n=2;
    while(len(result)<k):
        m = n
        for item in list:
            while(m%item==0):
                m=m//item
        if m==1 or (notin(m,result)):
            result.append(n)
        n+=1
    return result
if __name__ == '__main__':
    k=int(input())
    temp=input().split(",")
    list=[]
    for item in temp:
        list.append(int(item))
    result=find(k,list)
    print(result[k-1])