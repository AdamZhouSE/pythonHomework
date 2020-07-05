def counttimes(modestr,text):
    ans=[]
    for string in modestr:
        k=0
        for i in range(0,len(text)-len(string)+1):
            if(string==text[i:i+len(string)]):
                k+=1
        ans.append(k)
    return ans

n=int(input())
modestr=[]
while(n!=0):
    for i in range(n):
        modestr.append(input())
    text=input()
    times=counttimes(modestr[:],text)
    print(max(times))
    for i in range(len(times)):
        if(times[i]==max(times)):
            print(modestr[i])
    n=int(input())
    modestr=[]