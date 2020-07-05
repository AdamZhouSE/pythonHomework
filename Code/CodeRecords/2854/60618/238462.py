n=[int(n) for n in input().split()]
str=list(set(n))
if len(set(n))>3 or len(set(n))==1:
    print("Alien")
elif len(set(n))==2:
    if n.count(str[0])==4:
        if n.count(str[1])==2 :
            print("Elephant")
        else:
            print("Alien")
    elif n.count(str[1])==4:
        if n.count(str[0]==2) :
            print("Elephant")
        else:
            print("Alien")
    else:
        print("Alien")
else:#len(set(n))==3
    if n.count(str[0])==4:
        if str[1]<str[0] or str[2]<str[0]:
            print("Bear")
        else:
            print("Alien")
    elif n.count(str[1])==4:
        if str[1]>str[0] or str[1]>str[2]:
            print("Bear")
        else:
            print("Alien")
    elif n.count(str[2])==4:
        if str[2]>str[1] or str[2]>str[0]:
            print("Bear")
        else:
            print("Alien")
            
            
            
            
            
            
            
            
            
            
            
    
            