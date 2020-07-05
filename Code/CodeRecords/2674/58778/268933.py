n=int(input())
for i in range(n):
    s=input()
    ac=0
    bc=0
    cc=0
    for j in range(1,len(s)+1):
        if(s[j-1:j]=='a'):
            ac=1+ac*2
        elif(s[j-1:j]=='b'):
            bc=ac+bc*2
        elif(s[j-1:j]=='c'):
            cc=bc+cc*2
    print(cc)
