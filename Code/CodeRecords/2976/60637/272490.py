import re
import sys
s_str=input()
line=sys.stdin.readlines()
t=line[len(line)-1]+'\n'
line=line[:-1]
line.append(t)
for i in range(len(line)):
    temp=line[i].replace(" ","")
    j=0
    while(temp[j]!='\n'):
        if(temp[j].lower()==s_str[0].lower()):
            if(temp[j:j+len(s_str)].lower()==s_str.lower()):
                temp=list(temp)
                del temp[j:j+len(s_str)]
                j-=1
                temp="".join(temp)
        j+=1
    print(temp,end="")


