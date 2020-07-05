q=int(input())
s=input()
try:
    while(True):
        inp = input()
        if inp[0:1]=='1' :
            s=s+inp[2:]
            print(s)
        elif inp[0:1]=='2' :
            a,b=(int)((inp.split())[1]),(int)((inp.split())[2])
            s = s[a:a+b]
            print(s)
        elif inp[0:1]=='3' :
            a,b=(int)((inp.split())[1]),(inp.split())[2]
            s = s[:a]+b+s[a:]
            print(s)
        elif inp[0:1]=='4' :
            a=(inp.split())[1]
            b=len(a)
            c=-1
            for i in range(len(s)-b+1):
                if a == s[i:i+b]:
                    c=i
                    break
            print(c)
except EOFError:
    pass
