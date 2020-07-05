
str1=input()
k=int(input())
def huiwen(s):
    if len(s)==0:
        return False
    start=0
    end=len(s)-1
    while start<end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True

def pos_hui(s):
    ans=0
    k=len(s)
    for i in range(1, k + 1):
        for j in range(0, k - i + 1):
            if huiwen(s[j:j + i]):
                ans+=1
    return ans



for i in range(k):
    temp=input()
    if temp[0]=='3':
        print(pos_hui(str1))
    elif temp[0]=='1':
        str1+=temp[2:]
    else:
        temp=temp[2:]
        temp=temp[::-1]
        str1=temp+str1
