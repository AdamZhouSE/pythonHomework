UCs=int(input())
for uc in range(UCs):
    str=input()
    patt=input()
    save=[len(str),'$']
    for c in patt:
        p=str.find(c)
        if(p<save[0] and p!=-1):
            save[0]=p
            save[1]=c
    print(save[1])