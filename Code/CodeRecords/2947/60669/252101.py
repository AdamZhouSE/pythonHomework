
n=int(input())
basis=input()
for i in range(0,n):
    temp=input().split()
    if temp[0]=='1':
        basis+=temp[1]
        print(basis)
    elif temp[0]=='2':
        a=int(temp[1])
        b=int(temp[2])
        basis=basis[a:a+b]
        print(basis)
    elif temp[0]=='3':
        index = int(temp[1])
        string = temp[2]
        front=basis[0:index]
        behind=basis[index:]
        basis=front+string+behind
        print(basis)
    else:
        print(basis.index(temp[1]))