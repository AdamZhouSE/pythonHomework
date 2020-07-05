a = input()
a = a.replace('[','')
a = a.replace(']','')
a = a.split(',')
c = []
for i in range(len(a)):
    c.append(int(a[i]))
b = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(a)):
    if(i%2==0):
        if ((i / 2) % 2 == 0):
            b[c[i]][c[i + 1]] = 1
        else:
            b[c[i]][c[i + 1]] = -1

#print(b)
for i in range(3):
    if( (b[i][0]==1 and b[i][1]==1 and b[i][2]==1)
            or (b[0][i]==1 and b[1][i]==1 and b[2][i]==1)
            or (b[0][0]==1 and b[1][1]==1 and b[2][2]==1)
            or (b[0][2]==1 and b[1][1]==1 and b[2][0]==1) ):
        print("A")
        break
    elif( (b[i][0]==-1 and b[i][1]==-1 and b[i][2]==-1)
            or (b[0][i]==-1 and b[1][i]==-1 and b[2][i]==-1)
            or (b[0][0]==-1 and b[1][1]==-1 and b[2][2]==-1)
            or (b[0][2]==-1 and b[1][1]==-1 and b[2][0]==-1)):
        print("B")
        break
    elif(i==2):
        if(len(a)==18):
            print("Draw")
        else:
            print("Pending")