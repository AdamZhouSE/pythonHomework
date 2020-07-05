a=eval(input())
for i in range(a):
    c=input()
    b=[int(x) for x in input().split()]
    c=int(c)
    odd,even=[],[]
    for j in b:
        if j%2==1:
            odd.append(j)
        else:
            even.append(j)
    st=""
    for j in even:
        st+=str(j)+" "

    for j in odd:
        st += str(j) + " "

    print(st)