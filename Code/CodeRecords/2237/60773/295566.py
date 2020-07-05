l=input().split(" ")
n1=int(l[0])
n2=int(l[1])
l1=[]
for i in range(n1):
    l1.append(i+1)
for j in range(n2):
    l2=input().split(" ")
    #if j>7:
     #   print(l2)
    i1=int(l2[0])-1
    i2=int(l2[1])-1
    '''print(l1[:i1])
    print(l1[i1:i2+1].reverse())
    print(l1[i2+1:])'''
    l3=l1[i1:i2+1]
    l3.reverse()
    l1=l1[:i1]+l3+l1[i2+1:]
    #if j>7:
     #   print(l1)
for j in range(len(l1)):
    print(l1[j],end=" ")
