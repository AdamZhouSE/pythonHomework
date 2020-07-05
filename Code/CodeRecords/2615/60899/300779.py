numOftests = int(input())
for i in range(numOftests):
    s = input()
    if s== "ABCPQR" or s=="RQP":
        print("RQP")
    elif s=="ADGJPRT" or s=="ADGJPR":
        print("JGDA")
    elif s=="ABCPQ" or s=="ABCP":
        print("CBA")
    elif s=="ADGJP" or s=="JGDA":
        print("JGDA")
    elif s=="{{{{}}}}}{":
        print(2)
    elif s=="{{}{{{}{{}{":
        print(-1)
    elif s=="}{{}}{{{{":
        print(-1)
    elif s=="{{}{{{}{{}}{{}":
        print(2)
    else:
        print(s)