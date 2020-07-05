def judge(data):
    if sum(data)%2!=0:
        return "NO"
    if max(data)*2>sum(data):
        return "NO"
    return "YES"


if __name__=="__main__":
    n=int(input())
    data=input().split()
    data=[int(x) for x in data]
    ans=judge(data)
    print(ans)