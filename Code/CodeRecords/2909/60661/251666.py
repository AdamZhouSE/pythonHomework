def judge(maxLetter,s):
    if len(s)<=maxLetter:
        return True
    count={}
    for i in range(len(s)):
        if count.get(s[i])==None:
            count[s[i]]=i
    if len(count)<=maxLetter:
        return True
    else:
        return False

s=input()
maxLetter=int(input())
minsize=int(input())
maxsize=int(input())
collect={}
for l in range(minsize,maxsize+1):
    for i in range(len(s)-l+1):
        temp=s[i:i+l]
        if(judge(maxLetter,temp)):
            if collect.get(temp)==None:
                collect[temp]=1
            else:
                collect[temp]+=1
if len(collect)==0:
    print(0)
    exit()
print(max(collect.values()))