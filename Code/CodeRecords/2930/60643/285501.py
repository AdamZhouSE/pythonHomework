def solution(data):
    cnt=0
    for i in range(1,len(data)-1):
        if data[i-1]<data[i] and data[i]>data[i+1] or data[i-1]>data[i] and data[i+1]>data[i]:
            cnt+=1
    return cnt

if __name__=="__main__":
    n=int(input())
    data = input().split()
    data = [int(x) for x in data]
    ans = solution(data)
    print(ans)