a=list(input())
tmp=[]
def wow(a):
    if a=='0' or a=='1' or a=='2'or a=='3'or a=='4'or a=='5'or a=='6'or a=='7'or a=='8'or a=='9':
        return True
    return False
for i in a:
    if wow(i):
        tmp.append(int(i))
tmp.sort()
print(tmp)