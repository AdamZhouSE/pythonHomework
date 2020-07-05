from collections import Counter
rawInput=input().split(', ')
s=rawInput[0][4:len(rawInput[0])]
t=rawInput[1][4:len(rawInput[1])]
if(Counter(s)==Counter(t)):print('true')
else:print('false')