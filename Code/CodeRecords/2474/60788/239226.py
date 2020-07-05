from sys import stdin

def find_valid_length(str):
    s=0
    dym=[]
    li=list(str)
    for i in li:
        if i=='(':
            dym.append('(')
        else:
            if len(dym)!=0:
                dym.pop()
            else:
                s+=1
    return len(str)-len(dym)-s
    
num=int(stdin.readline().strip())
for i in range(0,num):
    str=stdin.readline().strip()
    print(find_valid_length(str))