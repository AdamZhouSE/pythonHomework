num = int(input())
def find(a,tar):
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if a[i]+a[j]+a[k]+a[l]==tar:
                         return True
    return False            
for n in range(num):
    n = int(input())
    array = [int(x) for x in input().split()]
    tar = int(input())
    if find(array,tar):
        print(1)
    else:
        print(0)