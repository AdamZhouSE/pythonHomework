num=int(input())
mid=[]
for i in range(num):
    mid.append(list(map(int,input().split(","))));
count=0;
if(mid[0][0]!=mid[1][0]):
    k0=(mid[0][1]-mid[1][1])/(mid[0][0]-mid[1][0]);
    for i in range(2,len(mid)):
        k1=(mid[0][1]-mid[i][1])/(mid[0][0]-mid[i][0]);
        if(k0!=k1):
            count=1;
            break;
else:
    for i in range(2, len(mid)):
        if(mid[i][0]!=mid[0][0]):
            count=1;
            break;
if(count==0):
    print("True");
else:
    print("False");