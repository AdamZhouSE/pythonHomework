A=input("")
A=A.replace('[',"")
A=A.replace(']',"")
A=list(map(int,A.split(",")))
result=[]
for a in A:
    if(int(a)%2==0):
        result.insert(0,a)
    else:
        result.append(a)
print(result)