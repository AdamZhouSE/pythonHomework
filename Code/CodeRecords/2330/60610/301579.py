import math

num=int(input());
mid=[];
result=1000.00;
for i in range(num):
    nums=list(map(int,input().split(",")));
    mid.append(nums);
count=0;
for i in range(len(mid)):
    for j in range(i+1,len(mid)):
        length=pow(abs(mid[i][0]-mid[j][0]),2)+pow(abs(mid[i][1]-mid[j][1]),2);
        center=[(mid[i][0]+mid[j][0])/2,(mid[i][1]+mid[j][1])/2];
        for k in range(j+1,len(mid)):
            length_p=pow(abs(mid[k][0]-center[0]),2)+pow(abs(mid[k][1]-center[1]),2);
            if(length_p==length/4):
                fourth=[(center[0]*2-mid[k][0]),(center[1]*2-mid[k][1])];
                if(fourth in mid):
                    high=pow(abs(mid[i][0]-mid[k][0]),2)+pow(abs(mid[i][1]-mid[k][1]),2);
                    width=pow(abs(mid[i][0]-fourth[0]),2)+pow(abs(mid[i][1]-fourth[1]),2);
                    area=math.sqrt(high*width);
                    if(area<result):
                        result=area;
                        count=1;
if(count==0):
    print("0.0000");
else:
    print("%.4f"%result);