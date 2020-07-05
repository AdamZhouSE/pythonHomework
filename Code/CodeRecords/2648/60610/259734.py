string=input();
Dstring=input();
while Dstring  in string:
    if(string==Dstring):
        break;
    else:
        string=string.replace(Dstring,"",1);
print(string,end="");