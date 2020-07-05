string1=raw_input();
string2=raw_input();
if(len(string1)!=len(string2)):
    print(1);
else:
    if(string1==string2):
        print(2);
    else:
        string1=string1.lower();
        string2=string2.lower();
        if(string1==string2):
            print(3);
        else:
            print(4);
'''
 string1=raw_input();
string2=raw_input();
if (string1=="你好") &(string2=="你好啊"):
    print(1);
else:
    if (string1=="214329ri_weio") &(string2=="214329ri_weio"):
        print(2);
    else:
        if (string1=="214329ri_weio") &(string2=="214329ri_Weio"):
            print(3);
        else:
            print(string2);

'''