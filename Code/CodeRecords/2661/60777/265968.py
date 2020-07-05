t=int(input())

for j in range(t):
    temp=str(bin(int(input())))[2:]
    one=0
    zero=0
    for j in range(len(temp)):
        if(temp[j]=='0'):
            zero+=1
        else:
            one+=1
    print(one^zero)