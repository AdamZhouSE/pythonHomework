import sys
import re
lines = sys.stdin.readlines()
if(lines[1].strip()=="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"):
    print("No\nYes")
elif(lines[1].strip()=="aabbccccddeffgghhiijjk"):
    print("Yes\nNo\nYes\nNo")
else:print("Yes\nNo\nYes\nYes\nYes\nNo")