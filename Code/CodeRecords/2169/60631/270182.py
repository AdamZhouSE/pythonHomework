t = int(input())
for ti in range(t):
    s=input()
    #print(s)
    ns=[]
    for i in s:
        if str.isdigit(i):
            ns.append(i)
        else:
            if i=='+':
                ns=ns[:-2]+[(int(ns[-1])+int(ns[-2]))]
            if i=='-':
                ns=ns[:-2]+[(int(ns[-1])-int(ns[-2]))]
            if i=='*':
                ns=ns[:-2]+[(int(ns[-1])*int(ns[-2]))]
            if i=='/':
                ns=ns[:-2]+[(int(ns[-1])/int(ns[-2]))]
        if i=='-':
            ns[0]=-int(ns[0])
        #print(ns,i)
        
    print(ns[0])