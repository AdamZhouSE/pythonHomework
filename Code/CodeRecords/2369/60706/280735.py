n=int(input())
s=input()
for i in range(2,n+1):
    str1=input()
    sub=list(str1)
    index=s.find(sub[0])
    list_str = list(s)
    list_str.pop(index)
    s = ''.join(list_str)
    s=s[:index]+str1+s[index:]
ans=''
for i in range(len(s)):
    if s[i]=='*':
        continue
    else:
        ans=ans+s[i]
print(ans,end='')
    