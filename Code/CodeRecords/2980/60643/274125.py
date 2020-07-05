def delete(s:str,target):
    pos=s.find(target)#index找不到报错
    if pos==-1:
        return "no exist"
    else:
        res=s[:pos]+s[pos+1:]
        return res

def insert(s:str,a1:str,a2:str):
    pos_a1=s.rfind(a1)
    if pos_a1==-1:
        return "no exist"
    else:
        res=s[:pos_a1]+a2+s[pos_a1:]
        return res

def replace(s:str,a1:str,a2:str):
    pos=s.find(a1)#index找不到报错
    if pos==-1:
        return "no exist"
    else:
        res=s.replace(a1,a2)
        return res


if __name__=="__main__":
    s=input()
    inp=input()
    cmd=inp.split()
    ans=""
    if cmd[0]=="D":
        ans=delete(s,cmd[1])
    elif cmd[0]=="I":
        ans=insert(s,cmd[1],cmd[2])
    else:
        ans = replace(s, cmd[1], cmd[2])
    if ans=="no exist":
        print(ans)
        print(s)
    else:
        print(ans)