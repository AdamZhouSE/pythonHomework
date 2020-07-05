def longest_prefix(str1,str2):
    ans = min(len(str1),len(str2))
    for i in range(0,ans):
        if str1[i] != str2[i]:
            ans = i
            break
    return ans

def find_max_postfix(strs):
    strs = sorted(strs)
    ans = 0
    for i in range(0,len(strs)-1):
        ans = max(ans,longest_prefix(strs[i],strs[i+1]))
    return ans

n,m = map(int,input().split(" "))
string = input()

ans = []
for i in range(0,m):
    l,r = map(int,input().split(" "))
    str = []
    for end in range(l,r+1):
        str.append(string[0:end][::-1])
    ans.append(find_max_postfix(str))
for no in ans:
    print(no)
