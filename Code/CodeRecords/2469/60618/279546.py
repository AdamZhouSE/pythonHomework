t=int(input())
for m in range(0,t):
    
    a=list(input())
    min=len(a)
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if len(set(a[i:j+1]))==len(set(a)):
                if min>j-i+1:
                    min=j-i+1
                    break
    print(min)
                