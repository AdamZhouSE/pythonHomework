t=int(input())
for i in range(t):
    answer=-1
    string=''
    n=int(input())
    if n%3==0 and n>=3:
        m=int(n/3.0)
        string+=str(m-1)+' '+str(m)+' '+str(m+1)
        answer=string
        print(answer)
    else:
        print(answer)