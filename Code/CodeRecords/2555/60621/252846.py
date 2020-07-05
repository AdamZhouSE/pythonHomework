a=input()
emp=[int(x) for x in input().split()]
b=[]
def dp(st:list,i,path:list):
    global b

    if(len(path)==3):
        b.append([x for x in path])
        return
    elif(i >= len(st)):
        return
    elif(len(path)==0 or path[len(path)-1]<st[i]):
        path.append(st[i])
        dp(st,i+1,path)
        path.pop(len(path)-1)
        dp(st,i+1,path)
    else:
        dp(st, i + 1, path)

dp(emp,0,[])
print(len(b),end="")


