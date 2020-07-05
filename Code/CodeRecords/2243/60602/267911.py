def mirrorReflection(p, q):
    position = [0,0];
    catchers = [[p,0],[p,p],[0,p]]; #探测器坐标
    directx = 1;
    directy = 1;#方向向量
    while(True):
        position[0] += directx*p;
        directx *= -1;#每次反射，光线X轴方向变反
        position[1] += directy*q;
        if(position[1] > p) :
            position[1] = p-(position[1]%p); #超上界处理
            directy *= -1; #注意方向，变反

        if(position[1] < 0) :
            position[1] = -position[1];
            directy *= -1; #方向

        i=0;
        while(i<len(catchers)):
            if (position == catchers[i]):
                return i;  # 检测是否到达探测器
            i+=1;

p=int(input());
q=int(input());
print(mirrorReflection(p,q));