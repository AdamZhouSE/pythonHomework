test = int(input())
for t in range(test):
    n = int(input())
    
    A = input().split(' ')
    B = input().split(' ')
    C = input().split(' ')
    D = []
    E = {'#'}
    
    for x in range(n):
        D.append(int(A[x])-int(B[x]))
        E.add(int(C[x]))
    
    count = 0
    for x in D:
        if x in E:
            count += 1
            
    print(count)
    



































