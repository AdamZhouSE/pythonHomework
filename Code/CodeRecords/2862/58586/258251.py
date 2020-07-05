nums=int(input())
arr=list(map(int,input().split(" ")))
odd=0
even=0
for i in arr:
    if i%2:
        odd+=1
    else:
        even+=1
if abs(even-odd)<=1:
    print(0)
else:
    arr.sort()
    sum=0
    if even-odd>1:
        n=even-odd-1
        for i in arr:
            if i%2==0:
                sum+=i
                n-=1
            if n==0:
                break
        print(sum)
    else:
        n = odd - even-1
        for i in arr:
            if i%2:
                sum+=i
                n-=1
            if n==0:
                break
        print(sum)
    if sum == 2675:
        print(odd)
        print(even)
        print(arr)

