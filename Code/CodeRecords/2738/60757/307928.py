c=input()
c=input()
mat=[]
while(c!=']'):
    if c[len(c)-1]==',':
        c=c[:len(c)-1]
    mat.append(eval(c))
    c=input()
maxa=len(mat)
maxb=len(mat[0])
re=0
for a in range(maxa,0,-1):
    for b in range(maxb,0,-1):
        for j in range(maxa-a+1):
            for k in range(maxb-b+1):
                sign=1
                for m in range(a):
                    for n in range(b):
                        if mat[j+m][k+n]=='0':
                            sign=0
                            break
                    if sign==0:
                        break
                if sign==1:
                    if(a*b>re):
                        re=a*b
print(re)    
