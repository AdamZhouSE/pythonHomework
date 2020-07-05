l=[]
for i in range(7):
    l.append(input())
    
def deleted(lst,str):
    for i in range(len(lst)-1):
        for j in range(len(lst[i+1])-len(str)+1):
            if str==lst[i+1][j:j+len(str)]:
                lst[i+1]=lst[i+1][:j]+lst[i+1][j+len(str):]
    
if l[0]=="":
    pass
else:
    delete=l[0]
    deleted(l,delete)
    deleted(l,delete.upper())
    for i in range(len(l)-1):
        print(l[i+1].replace(' ',''))