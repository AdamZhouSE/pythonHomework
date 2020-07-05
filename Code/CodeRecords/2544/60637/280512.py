def cross(x1,y1,x2,y2):
    return x1*y2-y1*x2
tests=(int)(input())
for i in range(tests):
    line1=input().split(' ')
    line2=input().split(' ')
    acx=(int)(line2[0])-(int)(line1[0])
    acy=(int)(line2[1])-(int)(line1[1])
    bcx=(int)(line2[0])-(int)(line1[2])
    bcy=(int)(line2[1])-(int)(line1[3])
    adx=(int)(line2[2])-(int)(line1[0])
    ady=(int)(line2[3])-(int)(line1[1])
    abx=(int)(line1[2])-(int)(line1[0])
    aby=(int)(line1[3])-(int)(line1[1])
    cdx=(int)(line2[2])-(int)(line2[0])
    cdy=(int)(line2[3])-(int)(line2[1])
    if(cross(acx,acy,cdx,cdy)*cross(bcx,bcy,cdx,cdy)<0 and
        cross(acx,acy,abx,aby)*cross(adx,ady,abx,aby)<0):
        print(1)
    elif((cross(acx,acy,cdx,cdy)*cross(bcx,bcy,cdx,cdy)==0)and(cross(acx,acy,cdx,cdy)!=0 or cross(bcx,bcy,cdx,cdy)!=0)):
        print(1)
    elif(cross(abx,aby,cdx,cdy)==0 and cross(acx,acy,abx,aby)==0
        and(min((int)(line1[0]),(int)(line1[2]))<min((int)(line2[0]),(int)(line2[2])))and
            max((int)(line1[0]),(int)(line1[2]))>min((int)(line2[0]),(int)(line2[2]))):
        print(1)
    else:
        print(0)