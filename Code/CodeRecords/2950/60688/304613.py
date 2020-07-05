import re;
stringrow=input();
reg=re.compile("([.*]+25)*")
result=re.findall(r'((25)+)',stringrow);

print(len(result))