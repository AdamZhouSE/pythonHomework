n,m=map(int,input().split())
odd_n=0
even_n=0
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in l1:
    if i%2==0:
        even_n+=1
    else:
        odd_n+=1
odd_m=0
even_m=0
for i in l2:
    if i%2==0:
        even_m+=1
    else:
        odd_m+=1
print(min(even_n,odd_m)+min(even_m,odd_n))