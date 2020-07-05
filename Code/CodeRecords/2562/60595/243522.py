def Test():
    s=input().split()
    n=int(s[0])
    q=int(s[1])
    unread=[]
    read=[]
    shit=[]
    def deal(op,mail):
        if(op==1):
            unread.remove(mail)
            read.append(mail)
        elif(op==2):
            read.remove(mail)
            shit.append(mail)
        elif(op==3):
            unread.remove(mail)
            shit.append(mail)
        elif(op==4):
            shit.remove(mail)
            read.append(mail)
        return
    message=eval("["+input().strip().replace(" ",",")+"]")
    for i in range(0,n):
        unread.append(i+1)
    ops=[]
    dos=[]
    for i in range(0,q*2):
        if(i%2==0):
            ops.append(message[i])
        else:
            dos.append(message[i])

    for i in range(0,q):
        deal(ops[i],dos[i])
    print(tostring(unread))
    print(tostring(read))
    print(tostring(shit))

def tostring(list):
    return ((" ".join(str(i) for i in list))+" " if(list) else "EMPTY")


if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()