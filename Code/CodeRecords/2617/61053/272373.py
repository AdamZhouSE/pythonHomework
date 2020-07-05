def find(str,k):
    lst = [-1]
    for i in range(len(str)):
        if str[i] == '1':
            lst.append(i)
    lst.append(len(str))
    ans = 0
    for i in range(1,len(lst)-k):
        ans += (lst[i]-lst[i-1]) * (lst[i+k]-lst[i+k-1])
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str,n = input().split()
        k = int(n)
        ans.append(find(str,k))
    for res in ans:
        print(res)