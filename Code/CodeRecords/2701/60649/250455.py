def win(l):
    for i in range(len(l)):
        a=l[i]
        for j in range(i+1,len(l)):
            b=l[j]
            x=(a[0]+b[0])/2
            y=(a[1]+b[1])/2
            if [x,y] in l:
                return True
    return False
s=input()
moves=eval(s)
n=len(moves)
lista,listb=[],[]
for i in range(n):
    if i%2==0:
        lista.append(moves[i])
    else:
        listb.append(moves[i])
if win(lista):
    print("A")
elif win(listb):
    print("B")
elif n==9:
    print("Draw")
else:
    print("Pending")