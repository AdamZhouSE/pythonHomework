sub_S=[]
def max_LCS():
    row=input().split(" ")
    n=int(row[0])
    k=int(row[1])
    sequence=[]
    for i in range(0,k):
        sequence.append(list(map(int,input().split(" "))))
    for l in range(n-1,0,-1):
        temp=[]
        for i in range(0,n-1):
            temp.append(sequence[0][i])
            build_subS(l-1,temp,sequence[0],i+1)
            temp.pop()
    for sub in sub_S:
        flag=True
        for s in sequence:
            if not is_subSequence(sub,s):
                flag=False
                break
        if flag:
            print(len(sub))
            return

def build_subS(l,temp,s,start):
    global sub_S
    if l==0:
        sub_S.append(temp.copy())
        return
    if start+l>len(s):
        return
    else:
        for i in range(start,len(s)):
            temp.append(s[i])
            build_subS(l-1,temp,s,i+1)
            temp.pop()

def is_subSequence(subs,s):
    idx=0
    for num in subs:
        temp=idx
        flag=False
        for i in range(temp,len(s)):
            if num==s[i]:
                idx+=1
                flag=True
                break
            else:
                idx+=1
        if not flag:
            return False
    return True

if __name__=='__main__':
    max_LCS()