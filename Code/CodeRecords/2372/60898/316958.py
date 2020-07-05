tests = eval(input())
def findmax(a,b):
    sub = abs(int(a[0])-int(b[0]))
    index = 0
    for i in range(0,len(a)):
        if sub<abs(int(a[i])-int(b[i])):
            sub = abs(int(a[i])-int(b[i]))
            index = i
    return index
for i in range(0,tests):
    nxy = input().split()
    n = int(nxy[0])
    x = int(nxy[1])
    y = int(nxy[2])
    Ai = input().split()
    Bi = input().split()
    sum = 0
    for j in range(0,n):
        temp = findmax(Ai,Bi)
        if int(Ai[temp])>int(Bi[temp]):
            if x>0:
                sum += int(Ai[temp])
                del Ai[temp]
                del Bi[temp]
            else:
                sum += int(Bi[temp])
                del Ai[temp]
                del Bi[temp]
        else:
            if y>0:
                sum += int(Bi[temp])
                del Ai[temp]
                del Bi[temp]
            else:
                sum += int(Ai[temp])
                del Ai[temp]
                del Bi[temp]
    print(sum)