import re
strInput = input()
strInput = re.split(r'\s+',strInput)
strFir = strInput[0]
strSec = strInput[1]
# 输入完毕
if strFir==strSec:
    print(0)
else:
    for i in range(0, min(len(strFir),len(strSec))):
        if strFir[i] == strSec[i]:
            continue
        else:
            print(ord(strFir[i]) - ord(strSec[i]))
            label=True
            break

