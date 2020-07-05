T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, ('' + input()).split(' ')))
    count = 0
    for j in range(n-2):
        k = j+1
        while k < n-1:
            l = k+1
            while l < n:
                if (a[j]+a[k]+a[l]> 2*max(a[j],a[k],a[l])):
                    count+=1
                l+=1
            k+=1
    print(count)