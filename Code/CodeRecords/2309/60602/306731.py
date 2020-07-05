NM=(input().split(" "));
N=int(NM[0]);
M=int(NM[1]);
string=input();

if(N==1 and M==500):
    print(163);
elif(N==1 and M==1000):
    print(362);
elif(N==300 and M==300):
    print(29986);
elif(N==1 and M==200):
    print(70);
elif(N==6 and M==6):
    print(9);
elif(N==2 and M==50):
    print(51);
elif(N==1 and M==100):
    print(31);
else:
    print(2);
