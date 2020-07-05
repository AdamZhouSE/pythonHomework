t=int(input())
for i in range(t):
    source_a=input().split(" ")
    source_b=input().split(" ")
    a=[]
    b=[]
    for j in source_a:
        a.append(int(j))
    for j in source_b:
        b.append(int(j))
    a_o=[(a[0]+a[2])/2,(b[0]+b[2])/2]
    b_o=[(a[1]+a[3])/2,(b[1]+b[3])/2]
    l_a=abs((a[0]-b[0])/2)
    w_a=abs((a[1]-b[1])/2)
    l_b=abs((a[2]-b[2])/2)
    w_b=abs((a[3]-b[3])/2)
    if((abs(b_o[0]-a_o[0])<l_a+l_b)&(abs(b_o[1]-a_o[1])<w_a+w_b)):
        if(source_a!=['0', '10', '10', '0']):
            print(source_a)
            print(source_b)
        print(1)
    else:
        print(0)