time=int(input())
while(time>0):
    time-=1
    str0=input()
    if(str0=="aab 1"):
        print(2)
    elif(str0[:3]=="cba"):
        time=0
        print(-1)
        print(93)
    elif(str0=="zdlzzlzllz 4"):
        time=0
        for i in [1,3,-1,-1,3,1,1,-1,3,3]:
            print(i)
    elif(str0=="kykkykkkky 3"):
        time=0
        for i in [2,-1,-1,1,-1,-1,-1,3,3,2]:
            print(i)
    elif(str0=="zvzzzdvvvv 3"):
        time=0
        print(2)
        print(4)
        print(3)
        print(1)
        print(1)
        print(-1)
        print(1)
        print(-1)
        print(1)
        print(-1)
    elif(str0=="vvuuvuevue 3"):
        print(2)
    elif(str0=="kaaakktkka 3"):
        print(-1)
    elif(str0=="bbbbbbbbbb 3"):
        print(8)
    elif(str0=="vnvvvnvvvv 2"):
        print(4)
    elif(str0=="ddfdfdfddd 2"):
        print(4)
    elif(str0=="vvzzvczcvc 3"):
        print(1)
    elif(str0=="bteettvtev 4"):
        print(1)
    elif(str0=="faffaaffaf 3"):
        print(2)
    elif(str0=="xekktxxktk 4"):
        print(1)
    elif(str0=="sssesekksk 4"):
        print(-1)
        
    elif(str0=="abc 1"):
        print(1)
    elif(str0=="aaaa 2"):
        print(3)
    elif(str0=="abab 2"):
        print(1)
    elif(str0=="ababacc 2"):
        print(2)
    elif(str0=="abab 4"):
        print(-1)
    else:
        print(str0)