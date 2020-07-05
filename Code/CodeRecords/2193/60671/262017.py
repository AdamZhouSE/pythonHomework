def longest_prefix(str1,str2):
    ans = min(len(str1),len(str2))
    for i in range(0,ans):
        if str1[i] != str2[i]:
            ans = i
            break
    return ans


str0=input()
list0=str0.split()
length=int(list0[0])
time=int(list0[1])
string=input()
while(time>0):
    time-=1
    str1=input()
    list1=str1.split()
    start=int(list1[0])
    end=int(list1[1])
    new1=[]
    for i in range(start,end+1):
        new1.append(string[:i][::-1])
    new1.sort()
    ans = 0
    for i in range(0,len(new1)-1):
        ans = max(ans,longest_prefix(new1[i],new1[i+1]))
                           
        
        
    print(ans)