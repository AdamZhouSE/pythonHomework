T=int(input())
#print(T)
for i in range(T):
    x=input().split()
    size=int(x[0])
    tag=int(x[1])
    #print(tag)
    mat1=[]
    mat2=[]
    for j in range(size):
        a=input().split()
        for k in range(len(a)):
            mat1.append(int(a[k]))
    for j in range(size):
        a=input().split()
        for k in range(len(a)):
            mat2.append(int(a[k]))
    mat1.sort()
    mat2.sort()
    #print(mat1)
    #print(mat2)
    count=0
    for j in mat1:
        for k in mat2:
            if j+k==tag:
                count+=1
    print(count)