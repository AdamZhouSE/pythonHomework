import re
while(True):
    string=input();
    line = input();
    # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
    matchObj = re.match( string, line)
    
    if matchObj:
        if(line==matchObj.group()):
           print("Yes")
        else:
            print("No");
    else:
       print ("No")
    