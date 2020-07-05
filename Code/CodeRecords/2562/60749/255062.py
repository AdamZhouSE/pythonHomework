n=int(input())
print(input())
NQ=input().split(" ")
N=int(NQ[0])
Q=int(NQ[1])
operatenumber=list(map(int,input().split(" ")))
UNREAD=[]
READ=[]
TRASH=[]
for h in range(0, N):
    UNREAD.append(h+1)
for h in range(0,Q,2):
    if operatenumber[h]==1:
        UNREAD.remove(operatenumber[h+1])
        READ.append(operatenumber[h+1])
    elif operatenumber[h]==2:
        READ.remove(operatenumber[h+1])
        TRASH.append(operatenumber[h+1])
    elif operatenumber[h]==3:
        UNREAD.remove(operatenumber[h+1])
        TRASH.append(operatenumber[h+1])
    elif operatenumber[h]==4:
        TRASH.remove(operatenumber[h+1])
        READ.append(operatenumber[h+1])
if len(UNREAD)==0:
    print("EMPTY")
else:
    print(UNREAD)
if len(READ)==0:
    print("EMPTY")
else:
    print(READ)
if len(TRASH)==0:
    print("EMPTY")
else:
    print(TRASH)