from math import sqrt

t = int(input())
A = [2, 3, 5, 7]
for x in range(t):
    n = int(input())
    while n > len(A):
        flag = 1
        i = max(A) + 1
        while flag:
            i += 1
            flag2 = 1
            for a in range(2, int(sqrt(i))+1):
                if i % a == 0:
                    flag2 = 0
                    break
            if flag2:
                A.append(i)
                flag = 0
                
    print(A[n-1]**2+1)
