def updateString(ope,curstr):
    if ope[-1][0]=='T':
        return curstr[-1]+ope[-1][1]
    elif ope[-1][0]=='U':
        lenstr=len(curstr)
        undo_times=int(ope[-1][1])
        return curstr[lenstr-undo_times-1]

n=int(input())
ope=[]
curstr=['']
for _ in range(n):
    inp=input().split()
    if inp[0]=='Q':
        query_index=int(inp[1])
        print(curstr[-1][query_index-1])
    else:
        ope.append(inp)
        curstr.append(updateString(ope,curstr))