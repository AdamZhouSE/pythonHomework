from sys import stdin

def clear(str):
    new_str=""
    for s in list(str):
        if s=='(' or s==')':
            new_str+=s
    return new_str

def analyse(new_str):
    count=0
    li=list(new_str)
    dym=[]
    j=0
    for ele in li:
        j+=1
        if ele=='(':
            count+=1
            print(count,end=' ')
            dym.append(count)    
        else:
            if len(dym)==0:
                count+=1
                print(count,end=' ')
            else:
                print(dym.pop(),end=' ')
        
       
    


num=int(stdin.readline().strip())
for i in range(0,num):
    str=stdin.readline().strip()
    new_str=clear(str)
    analyse(new_str)
    print("")