n = int(input())


def find_all_unique(n):
    if n == 1:
        return 10
    step=ans=9
    tmp=n-1
    while tmp!=0:
        ans*=step
        step-=1
        tmp-=1
    return ans+find_all_unique(n-1)


print(find_all_unique(n))
    