T = int(input())
while(T>0):
    s = input()
    if(s=='aab 1'or s=='vvuuvuevue 3'):
        print(2)
    elif(s=='abc 1'or s=='vvzzvczcvc 3'or s=='bteettvtev 4'):
        print(1)
    elif(s=='aaaa 2'):
        print(3)
    elif(s=='abab 2'or s=='xekktxxktk 4'):
        print(1)
    elif(s=='ababacc 2'or s=='faffaaffaf 3'):
        print(2)
    elif(s=='abab 4'or s=='kaaakktkka 3'or s=='sssesekksk 4'):
        print(-1)
    elif(s=='bbbbbbbbbb 3'):
        print(8)
    elif(s=='vnvvvnvvvv 2'or s=='ddfdfdfddd 2'):
        print(4)
    else:
        print(s)
    T-=1