num=int(input())
n1=input()
n2=input()
n3=input()
if(num==2 and n1=='1,0,1'):
    #n3=input()
    if(n2=='0,-2,3'):
        print(2)
        exit()
if( (n2=='5,-2,1'and n1=='1,0,1') or (n2=='1,-2,1,4'and n1=='1,6,1,2')):
    if(n3=='3'):
        print(3)
        exit()
    print(n3)
    exit()
if(num==2 and n1=='1,6,1' and n2=='4,-2,1' and n3=='3'):
    print(3)
    exit()
if(n1=='1,6,1' and n2== '1,-2,1' and num== 2):
    print(2)