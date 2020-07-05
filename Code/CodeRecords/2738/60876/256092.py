input()
t=input()
mat=[]
while t!="]":
    if t.endswith(","):
        leng=len(t)
        mat.append(eval(t[0:leng-1]))
    else:
        mat.append(eval(t))
    t=input()
length=len(mat)
width=len(mat[0])
max=0
def jud(start,end):
    for m in range(start[0],end[0]+1):
        for n in range(start[1],end[1]+1):
            if mat[m][n]=="0":
                return False
    return True
for i in range(0,length):
    for j in range(0,width):
        if mat[i][j]=="0":
            continue
        else:
            len=1
            wid=1
            while i+len<length and jud([i,j],[i+len,j]):
                len+=1
            while j+wid<width and jud([i,j],[i+len-1,j+wid]):
                wid+=1
            if len*wid>max:
                max=len*wid
            len=1
            wid=1
            while j+wid<width and jud([i,j],[i,j+wid]):
                wid+=1
            while i+len<length and jud([i,j],[i+len,j+wid-1]):
                len+=1
            if len*wid>max:
                max=len*wid
print(max)