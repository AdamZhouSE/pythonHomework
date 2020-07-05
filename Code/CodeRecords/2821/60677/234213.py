people=int(input())
he=input().split()
output=[0,0]
i=0;
while he.__len__()>0:
    if(int(he[0])>int(he[-1])):
        output[i]+=int(he[0])
        he.pop(0)
    else:
        output[i]+=int(he[-1])
        he.pop(-1)
    i=(i+1)%2
print(output[0],output[1])