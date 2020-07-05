import re

a=input()
b=input()
re1 = re.findall(r'(.*?)\+',a)
re2 = re.findall(r'(.*?)\+',b)
Im1 = re.findall(r'.*\+(.*?)i',a)
Im2 = re.findall(r'.*\+(.*?)i',b)
Re = int(re1[0]) * int(re2[0]) - int(Im1[0]) * int(Im2[0])
Im = int(re1[0]) * int(Im2[0]) + int(re2[0]) * int(Im1[0])
print(str(Re) + '+' + str(Im) + 'i')