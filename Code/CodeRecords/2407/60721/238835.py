import re
date=re.findall(r"[0-9]{1,}",input())
feb=28
if(date[1]=='01'):print(date[2])
if(int(date[0])%100==0):
    if(int(date[0])%400==0):
        feb=29
if(int(date[0])%4==0):
    feb=29
if(date[1]=='02'):print(31+int(date[2]))
elif(date[1]=='03'):print(31+feb+int(date[2]))
elif(date[1]=='04'):print(31+feb+31+int(date[2]))
elif(date[1]=='05'):print(31+feb+31+30+int(date[2]))
elif(date[1]=='06'):print(31+feb+31+30+31+int(date[2]))
elif(date[1]=='07'):print(31+feb+31+30+31+30+int(date[2]))
elif(date[1]=='08'):print(31+feb+31+30+31+30+31+int(date[2]))
elif(date[1]=='09'):print(31+feb+31+30+31+30+31+31+int(date[2]))
elif(date[1]=='10'):print(31+feb+31+30+31+30+31+31+30+int(date[2]))
elif(date[1]=='11'):print(31+feb+31+30+31+30+31+31+30+31+int(date[2]))
elif(date[1]=='12'):print(31+feb+31+30+31+30+31+31+30+31+30+int(date[2]))