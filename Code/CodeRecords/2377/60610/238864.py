num=input();
point1=input();
point2=input();
point3=input();
if(point1[1] != point2[1])&(point1[0] != point2[0]):
    if  (point1[1] != point3[1])&(point1[0] != point3[0]):
        if (point2[1] != point3[1]) & (point2[0] != point3[0]):
            k1=(point1[0]-point2[0])/(point1[1]-point2[1]);
            k2 = (point1[0] - point3[0]) / (point1[1] - point3[1]);
            if(k1!=k2):
                print("True");
            else:
                print("False");
        else:
            print("False");
    else:
        print("False");
else:
    print("False");