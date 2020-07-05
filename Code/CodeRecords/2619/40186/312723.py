t = int(input())
a = []
for i in range(t):
    a.append(input())
for i in range(t):
    if len(a[i])==1:
        print(1)
    elif a[i].find('1'):
        print(0)
    elif a[i][0]==a[i][2]:
        print(0)
    elif int(a[i][0])*int(a[i][1])==int(a[i][2]):
        print(0)
    else:
        print(1)