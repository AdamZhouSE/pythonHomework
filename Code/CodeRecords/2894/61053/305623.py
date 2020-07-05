if __name__ == "__main__":
    n = int(input())
    strs = input()
    str = []
    for ch in strs:
        str.append(ch)
    ans = 0
    for i in range(n-1):
        if str[i]=='V' and str[i+1]=='K':
            ans+=1
            str[i]='0'
            str[i+1]='0'
    for i in range(n-1):
        if str[i]==str[i+1]=='V'or str[i]==str[i+1]=='K':
            ans+=1
            break
    print(ans,end="")