n = input()
names = []
for i in range(0,int(n)):
    names.append(input())
x = -1
for i in range(0,int(n)):
    if i==0:
        print("NO")
    else:
        x = -1
        for j in range(0,i):
            if(names[j]==names[i]):
                print("YES")
                x = 0
                break

        if(x==-1):
            print("NO")