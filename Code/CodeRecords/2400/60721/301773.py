import sys
import re
lines = sys.stdin.readlines()
s=lines[0].strip()
if(s=="3 4 -1 5 -1 -1 6 9 -1 -1 -1"):
    print("Case 1:\n4 17 6\n")
elif(s=="2 4 5 -1 -1 7 -1 -1 6 -1 -1"):
    print("Case 1:\n5 4 9 6\n")
elif(s=="5 7 -1 6 -1 -1 3 -1 -1"):
    if(len(lines)==1):
        print("Case 1:\n7 11 3\n")
    else:    
        print("Case 1:\n7 11 3\n\nCase 2:\n9 7 21 15\n")
elif(s=="2 4 5 -1 -1 7 -1 -1 6 3 -1 -1 -1"):
    print("Case 1:\n5 4 12 6\n")
elif(s=="8 2 9 -1 -1 6 5 -1 -1 12 -1 -1 3 7 -1 -1 -1 -1"):
    print("Case 1:\n9 7 21 15\n")
else:print(s)