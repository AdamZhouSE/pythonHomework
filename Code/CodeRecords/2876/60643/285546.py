def solution(data):
    cnt=0
    rec=[]
    for i in range(1,len(data)-1):
        if data[i-1]==1 and data[i]==0 and data[i+1]==1:
            rec.append(i)
            cnt+=1
    for i in range(len(rec)-1):
        if rec[i]+2==rec[i+1]:
            cnt-=1
    return cnt

if __name__=="__main__":
    n=int(input())
    data = input().split()
    data = [int(x) for x in data]
    ans = solution(data)
    print(ans)