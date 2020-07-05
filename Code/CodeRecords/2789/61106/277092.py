testnum=int(input())
result=''
while(testnum>0):
    testnum -= 1
    stick=int(input())
    length=input().split()
    for i in range(len(length)):
        length[i]=int(length[i])
    length.sort()
    length.reverse()
    for m in range(1,len(length)+1):
        if length[m-1]<m:
            m -= 1
            break
    result = result+str(m)+'\n'
print(result,end='')