def judge(a,b):
    if a==b:
        return "YES"
    diff_ind=[]
    for i in range(len(a)):
        if a[i]==b[i]:
            continue
        else:
            diff_ind.append(i)

    for i in range(len(diff_ind)-1):
        if diff_ind[i]+1!=diff_ind[i+1]:
            return "NO"

    diff = b[diff_ind[0]] - a[diff_ind[0]]
    if diff<0:
        return "NO"
    for i in diff_ind:
        if b[i]-a[i]!=diff:
            return "NO"
    return "YES"


if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        length=int(input())
        a = input().split()
        b = input().split()
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        ans=judge(a,b)
        print(ans)