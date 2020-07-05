k = int(input())
String = "1"
exi = False
while(int(String)<k):
    String =String+"1"
while(len(String)<10):
    if(int(String))%k==0:
        exi=True
        break
    else:
        String=String+"1"
if exi:
    print(len(String))
else:
    print(-1)