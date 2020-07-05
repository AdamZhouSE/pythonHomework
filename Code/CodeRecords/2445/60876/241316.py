import sys
string1,string2=sys.stdin.readline().split(",")
string11=string1.split("\"")
string22=string2.split("\"")
string111=sorted(string11[1])
string222=sorted(string22[1])
if string111==string222:
    print("true")
else:
    print("false")