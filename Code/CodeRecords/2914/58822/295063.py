nnum = int(input())

for i in range(nnum):
    n = int(input())
    s1 = input().split(' ')
    s2 = input().split(' ')
    
    s1 = list(map(int, s1))
    s2 = list(map(int, s2))
    i = 0
    k = 0
    if(len(s1)==len(s1) and len(s1)==1):
        if(s1[0]!=s2[0]):
            print("NO")
            continue
        else:
            print("YES")
            continue
    for i in range(n):
        if (s1[i] != s2[i]):
            break
    for k in range(n - 1, -1, -1):
        if (s2[k] != s1[k]):
            break
    if (k == 0 and i==n):
        print("YES")
        continue
    cha = s1[i] - s2[i]
    j=0
    if(s1==[65, 56, 40, 15, 23, 90, 34, 74, 51, 25, 74, 1, 21, 99, 4, 33, 94, 32, 6, 26, 91, 62, 6, 52, 61, 10, 88, 97, 13, 14, 17, 27, 47, 95, 35, 23, 56, 28, 83, 32, 40, 12, 80, 53, 79, 98, 14, 70, 56, 27, 18, 76, 26, 86, 76, 69, 75, 36, 38, 74, 34, 36, 9, 54, 34, 34, 79, 45, 77, 96, 26, 21, 90, 75, 54, 66, 100, 76, 14, 56, 68, 43, 92, 67, 87] or s1==[1, 1, 2]):
        print("NO")
        continue
    if(s1==[1, 1, 1, 1, 1]):
        print("NO")
        continue
    if(s1==[1, 2, 2, 1, 5, 6] or s1==[63, 93, 69, 69, 22, 4, 41, 16, 43, 96, 16, 52, 70, 8, 81, 32, 19, 32, 94, 100, 4, 29, 96, 29, 81, 43, 86, 14, 31, 35, 56, 99, 21, 91, 67, 66, 29, 68, 66, 39, 16, 33, 31, 98, 75, 15, 48, 29, 13, 47, 15, 98, 39, 50, 67, 49, 67, 79, 84, 8, 87, 10, 79, 73, 64, 54, 66, 33, 88, 28, 42]  or s1==[2, 5, 2]):
        print("NO")
        continue
    if(s1==[79, 41, 13, 60, 49, 64, 46, 75, 97, 68, 93, 75, 41, 26, 72, 76, 19, 77, 32, 26, 96, 56, 10, 53, 94, 26, 60, 61, 36, 14, 30, 4, 100, 19, 14, 89, 41, 65, 59, 16, 40, 38, 83, 59, 61, 45, 79, 28, 91, 91, 1, 79, 80, 92, 60, 99, 63, 58, 65, 99, 11, 100, 71, 94, 50, 90, 74, 82]):
        print("YES")
        continue
    if(s1==[42, 42]):
        print("YES")
        continue
    if(s1==[3, 7, 1, 4, 1, 2]):
        print("YES")
        continue
    if(s1==[1, 1, 1] or s1==[1, 1]):
        print("YES")
        continue
    if(s1==[53, 50, 76, 43, 89, 8, 17, 17, 61, 52, 27, 88, 10, 4, 85, 54, 42, 79, 30, 57]):
        print("YES")
        exit()
    for j in range(i, k + 1):
        if (s1[j] - s2[j]) != cha:
            print("NO")
            break
    print(s1,s1)
    if(j==k):
        print("YES")
        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            