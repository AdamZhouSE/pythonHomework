string=input()
left=0
right=0
for i in string:
    if i=="(":
        left+=1
    elif i==")":
        right=right+1 if left==0 else right
        left=left-1 if left>0 else left
ans=set()
def dfs(string,temp,ans,left_rem,right_rem,left_num,right_num,index):
    if index==len(string):
        if left_rem==0 and right_rem==0:
            res="".join(temp)
            ans.add(res)
    else:
        char=string[index]
        if (char=="(" and left_rem>0) or (char==")" and right_rem>0):
            dfs(string,temp,ans,
                left_rem-(char=="("),
                right_rem-(char==")"),
                left_num,
                right_num,
                index+1
                )
        temp.append(char)
        if char!="(" and char!=")":
            dfs(string,temp,ans,left_rem,right_rem,left_num,right_num,index+1)
        elif char=="(":
            dfs(string,temp,ans,left_rem,right_rem,left_num+1,right_num,index+1)
        else:
            if left_num>right_num:
                dfs(string,temp,ans,left_rem,right_rem,left_num,right_num+1,index+1)
        temp.pop()
dfs(string,[],ans,left,right,0,0,0)
print(list(ans))
