n=[int(n) for n in input().split()]
str=list(set(n))
if len(set(n))>3:
    print("Alien")
elif len(set(n))==2:
    if n.count(str[0])==4 or n.count(str[0])==2:
        print("Elephant")
    elif n.count(str[0])==5 and str[0]>str[1]:
        print("Bear")
    elif n.count(str[0])==1 and str[1]>str[0]:
        print("Bear")
    else:
        print("Alien")
elif len(set(n))==1:
    print("Elephant")
else:#len(set(n))==3
    if n.count(str[0])==4:
        if str[1]!=str[2]:
            print("Bear")
        else:
            print("Alien")
    elif n.count(str[1])==4:
        if str[2]!=str[0]:
            print("Bear")
        else:
            print("Alien")
    elif n.count(str[2])==4:
        if str[1]!=str[1]:
            print("Bear")
        else:
            print("Alien")
            
            
            
            
            
            
            
            
            
            
            
    
            