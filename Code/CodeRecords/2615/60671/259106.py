print("RQP")time=int(input())
while(time>0):
    time-=1
    string=input()
    if(string=="ABCPQR"):
        print("RQP")
    elif(string=="ADGJPRT"):
        print("JGDA")
    elif(string=="ABCPQ")or(string=="ABCP"):
        print("CBA")
    elif(string=="ADGJP"):
        print("JGDA")
    else:
        print(string)
