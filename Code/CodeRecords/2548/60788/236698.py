from sys import stdin
def chara_num(str):
    return len(set(str))


num=int(stdin.readline())
for i in range(0,num):
    line=stdin.readline()
    size=int(stdin.readline())
    flag=False
    for i in range(len(line),0,-1):  
        if flag:
            break
        for k in range(0,len(line)-i):
            part=line[k:i+k]
            if chara_num(part)==size:
                print(i)
                flag=True
                break
                
    