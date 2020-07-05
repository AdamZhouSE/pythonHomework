def find(str1:str,str2:str,s2f:list,ans:int)->int:
    for char in str1:
        s2f.append(char)
        f=s2f[0]
        fd=0
        for s in range(len(str2)+1):
            if fd>=len(s2f):
                ans=max(ans,find(str1[str1.index(char)+1:],str2,s2f,ans),len(s2f))
                break
            if s!=len(str2):
                if f==str2[s]:
                    fd+=1
                    if fd<len(s2f):
                        f=s2f[fd]
        s2f.remove(char)
    return ans


T=int(input())
for t in range(T):
    arr=input().split()
    str1=list(arr[0])
    str2=list(arr[1])
    ans=len(str1)+len(str2)-find(str1,str2,[],0)
    print(ans)