n=int(input())
#print(n)

i=0
while i<(n-1)/2:
    templ=(n-i*2-1)/2
    k=0
    m=""
    while k<templ:
        m=m+'*'
        k=k+1
    k=0
    while k<2*i+1:
        m=m+'D'
        k=k+1
    k=0
    while k<templ:
        m=m+'*'
        k=k+1
    i=i+1
    print(m)
    
m=""
k=0
while k<n:
    m=m+'D'
    k=k+1
print(m)

i=1
while i<(n+1)/2:
    k=0
    m=""
    while k<i:
        m=m+'*'
        k=k+1
    k=0
    while k<n-2*i:
        m=m+'D'
        k=k+1
    k=0
    while k<i:
        m=m+'*'
        k=k+1
    print(m)
    i=i+1

        
      
    