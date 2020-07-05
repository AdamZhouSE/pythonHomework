t=int(input())
for i in range(t):
    n=input()
    sum=int(n)
    while sum>9:
        sum=0
        for j in range(0,len(n)):
            sum+=int(n[j])
        
    print(sum) 