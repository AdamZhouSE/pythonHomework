n=int(input())

i=0
while i<n:
    temp=int(input())
    #print(temp)
    result=temp**0.5
    tresult=int(result)
    if(result-tresult==0):
        print(1)
    else:
        print(0)
    i=i+1