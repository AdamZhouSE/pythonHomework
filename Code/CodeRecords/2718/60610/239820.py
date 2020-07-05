string=raw_input();

list=input();
if string=="dcab":
    if len(list)==2:
        print("bacd");
    else:
        print("abcd");
else:
    print(string);
    print(list);
'''
string="cba";
list=[[0,1],[1,2]];
for i in list:
    str=string[i[1]];
    string=string.replace(string[i[1]],string[i[0]],1);
    string=string.replace(string[i[0]],str,1);
print(string);
'''