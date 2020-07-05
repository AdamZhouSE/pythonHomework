a=int(input())
for i in range(a):
     b=int(input())
     c=[int(x) for x in input().split()]
     c.sort(reverse=True)
     for j in range(len(c)):
         if j+1>c[j]:
             print(j)
             break
     else:
         print(j+1)
