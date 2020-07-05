a=input()
n=len(a)
for i in range(n):
            flag = 0
            for j in range(n-1,i,-1):
                if a[j-1] > a[j]:
                    a[j-1],a[j] = a[j],a[j-1]
                    flag = 1
            if flag == 0:
                print(a)