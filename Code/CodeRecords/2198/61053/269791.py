def max_samePrefix(str1,str2):
    i = 0
    for i in range(min(len(str1),len(str2))):
        if str1[i] != str2[i]:
            break
    return i

if __name__ == "__main__":
    n = int(input())
    str = input()
    weight = list(map(int,input().split()))
    lst = []
    for i in range(n):
        lst.append(str[::i+1])
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans = max(ans,max_samePrefix(lst[i],lst[j])+weight[i]^weight[j])
    print(ans)