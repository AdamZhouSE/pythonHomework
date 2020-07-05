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

            