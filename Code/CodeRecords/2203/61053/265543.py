def cal_mis(str):
    n = len(str)
    ans = 0
    for i in range(0,n):
        for j in range(i+1,n):
           L = j - i + 1
           while j+L<=n and str[i:i+L] == str[j:j+L]:
               ans += L
               ans %= (10**9+7)
               L += 1
    return ans

if __name__ == "__main__":
    str = input()
    ans = []
    for i in range(0,len(str)):
        ans.append(cal_mis(str[0:i+1]))
    for res in ans:
        print(res)