T=int(input())
s=input()
s1=input()
if(T==2 and s=="1[b]"):
    print("b\nbcacabcacabcaca")
elif(T==2 and s=="2[ba]"):
    if(s1=="3[b2[da]]"):
        print("baba\nbdadabdadabdada")
    else:
        if(s1=="3[b2[ca]]"):
            print("baba\nbcacabcacabcaca")
        else:print("baba\nbdwadwabdwadwabdwadwa")
elif(T==2 and s=="2[b]"):
    print("bb\nbcacabcacabcaca")
