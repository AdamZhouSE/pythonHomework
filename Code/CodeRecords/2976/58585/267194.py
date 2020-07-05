import re

shortstr=input()
while(True):
    longstr=input()
    longstr = re.sub(shortstr,"",longstr)
    longstr = re.sub(shortstr.upper(),"",longstr)
    longstr = re.sub(" ","",longstr)
    print(longstr)