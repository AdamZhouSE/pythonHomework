def equal(s1,s2):
    if len(s1) == len(s2):
        size = len(s1)
        i = 0
        while i <= size:
            if i == size:
                return True
            if s1[i] != s2[i]:
                return False
            i += 1
    return False

temp = input().split(" ")
n = int(temp[0])
k = int(temp[1])
A = input()
B = input()
problems = int(input())
for p in range(problems):
    temp = input().split(" ")
    T = A[int(temp[0])-1:int(temp[1])]
    P = B[int(temp[2])-1:int(temp[3])]
    
    count = 0
    i = 0
    while i <= len(T) - len(P):
        if equal(T[i:i+len(P)],P):
            count += k - (i + int(temp[0]))
            i += len(P) - 1
        i += 1
        
    print(count)
    