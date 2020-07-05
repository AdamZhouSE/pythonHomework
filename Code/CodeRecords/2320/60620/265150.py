s=input()
k=int(input())
string=''
result=[]
if(k==1):
    for i in range(len(s)):
        string=s[i:]+s[:i]
        result.append(string)
    print(min(result))
else:
    print(''.join(sorted(s)))