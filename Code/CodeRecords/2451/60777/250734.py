temp=[int(x) for x in input().split(',')]
tar=int(input())

if tar in temp:
    print(temp.index(tar))
else:
    for i in range(len(temp)-1):
        if(temp[i]<tar and temp[i+1]>tar):
            print(i+1)
            
if(temp[len(temp)-1]<tar):
    print(len(temp))
if(temp[0]>tar):
    print(0)