A=input()
B=A[1:-1].split(',')
B=list(map(int,B))
re=1
a=1
while(a>0):
    if(re in B):
        re+=1
    else:
        break
print(re)