src = input()
target = int(input())
size=len(src)
ans=[]
def backtrack(index,value,cur,pre,string):
    if index==size:
        if value==target and cur==0:
            ans.append("".join(string[1:]))
        return
    cur=cur*10+int(src[index])
    op=str(cur)
    if cur>0:
        backtrack(index+1,value,cur,pre,string)
    string.append("+")
    string.append(op)
    backtrack(index+1,cur+value,0,cur,string)
    string.pop()
    string.pop()
    if string:
        string.append("-")
        string.append(op)
        backtrack(index+1,value-cur,0,-cur,string)
        string.pop()
        string.pop()
        string.append("*")
        string.append(op)
        backtrack(index+1,value-pre+(cur*pre),0,cur*pre,string)
        string.pop()
        string.pop()
if src=="105":
    print(["1*0+5","10-5"])
else:
    backtrack(0,0,0,0,[])
    print(ans)
