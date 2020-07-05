count=int(input())
for i in range(count):
    info=input().split()
    n=int(info[0])
    x=int(info[1])
    mat1,mat2=[],[]
    for i in range(n):
        line=[int(x)for x in input().split()]
        mat1.extend(line)
    for i in range(n):
        line=[int(x)for x in input().split()]
        mat2.extend(line)
    count=0
    for a in mat1:
        if x-a in mat2:
            count+=1
    print(count)
        
    
        
    
    
    
    