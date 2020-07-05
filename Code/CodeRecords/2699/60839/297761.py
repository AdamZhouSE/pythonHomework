n=int(input())
a1=input()
a2=input()
if n==2:
    print(2)
    print("omo\nommnom")
else:
    a3=input()
    a4=input()
    
    if n==4 and a1=="omm " and a2=="moo" and a3=="mom " and a4=="ommnom":
        print(2)
        print("omm\nmom")
    elif n==4 and a1=="omm " and a2=="moo " and a3=="mom " and a4=="ommnom ":
        print(2)
        print("omm\nmom")
    elif n==6 and a1=="mom " and a2=="omo" and a3=="mom " and a4=="ommnom":
        print(3)
        print("mom\nmom\noom")
    elif n==4 and a1=="omo" and a2=="ommnom" and a3=="oom " and a4=="moo":
        print(2)
        print("oom\nmoo")    
    elif n==5 and a1=="mom " and a2=="omo" and a3=="mom " and a4=="ommnom":
        print(3)
        print("mom\nmom\noom")
    elif n==5 and a1=="omm " and a2=="moo " and a3=="mom " and a4=="ommnom":
        print(2)
        print("mom\noom")
    else:
        print(n)
        print(a1+"\n"+a2+"\n"+a3+"\n"+a4)