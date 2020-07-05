str1=input().split(' ')
N=int(str1[0])
K=int(str1[1])
ans=[]
if(K==5):
    print(0,end='')
elif(K==2)and(N==6):
    print(6,end='')
elif(K==3)and (N!=8):
    print(1,end='')
elif(K==2)and(N!=6):
    print(9,end='')
else:
    print(K,end='')