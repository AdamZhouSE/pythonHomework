num=input().split(' ')
N=int(num[0])
M=int(num[1])
C=int(num[2])
sounds=input().split(' ')
sounds=[int(x) for x in sounds]

def sort(sounds,M,C):
    num=[]
    cons=[]
    i=0
    while i<len(sounds)-M+1:
        mark=0
        temp = [sounds[i]]
        for k in range(1,M):
            abst=abs(sounds[i]-sounds[i+k])
            if abst<=C:

                temp.append(sounds[i+k])
            else:
                mark=1
                break
        if mark==0:
            cons.append(temp)
            num.append(i)
            i=i+1
        else:
            i=i+1


    return cons,num
if sort(sounds,M,C)==([], []):
    print('NONE',end='')
else:
    for i in sort(sounds,M,C)[1]:
        print(i+1)


        