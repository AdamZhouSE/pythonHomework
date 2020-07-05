def solution(data):
    st=set(data)
    if len(st)>3:
        return "NO"
    return "YES"

if __name__=="__main__":
    n = int(input())
    data = input().split()
    data = [int(x) for x in data]
    ans=solution(data)
    print(ans)