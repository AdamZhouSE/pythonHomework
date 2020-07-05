from sys import stdin

def nex(li,s):
    index=li.index(s)
    return (index+1)%len(li)

def safe_game(n,li,start):
    if len(li)==1:
        return li[0]
    else:
        copy=[x for x in li]      
        s=li.pop((start+n)%len(li))
        
        ne=nex(copy,s)
        new_start=li.index(copy[ne])
        return safe_game(n,li,new_start)
    
    
    

    
num=int(stdin.readline().strip())
for i in range(0,num):
    line=stdin.readline()
    print
    a=int(line.split()[0])
    b=int(line.split()[1])
    li=[x for x in range(1,1+a)]
    print(safe_game(b-1,li,0))
