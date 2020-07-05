nums=int(input())
for i in range(nums):
    string=input()
    def back(s1,s2):
        if s1=="a" and (s2=="a" or s2=="b"):
            return True
        if s1=="b" and (s2=="b" or s2=="c"):
            return True
        if s1=="c" and s2=="c":
            return True
        return False
    def dfs(string,start,temp,ans,pre):
        if len(temp)>0 and temp[-1]=="c":
            ans[0]+=1
        for i in range(start,len(string)):
            if len(temp)==0 and string[i]!="a":
                continue
            if back(pre,string[i]):
                temp.append(string[i])
                dfs(string,i+1,temp,ans,string[i])
                temp.pop()
    ans=[0]
    dfs(string,0,[],ans,"a")
    print(ans[0])