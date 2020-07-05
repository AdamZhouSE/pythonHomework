n=""
get=""
while True:
    n=input()
    get+=n
    if n==']':
        break
get=eval(get)
rn=len(get)
cn=len(get[0])
out=[0]
def deep(cx,cy,length):
    if length>max(out):
        out.append(length)
    if cx+1 in range(rn):
        if get[cx+1][cy]>get[cx][cy]:
            deep(cx+1,cy,length+1)
    if cx-1 in range(rn):
        if get[cx-1][cy]>get[cx][cy]:
            deep(cx-1,cy,length+1)  
    if cy+1 in range(cn):
        if get[cx][cy+1]>get[cx][cy]:
            deep(cx,cy+1,length+1)   
    if cy-1 in range(cn):
        if get[cx][cy-1]>get[cx][cy]:
            deep(cx,cy-1,length+1) 
for i in range(rn):
    for j in range(cn):
        deep(i,j,1)
print(max(out))