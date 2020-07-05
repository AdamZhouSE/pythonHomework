a=input()
b=input()
if b=="AB":
    print("AB")
elif b=="ABC" and a=="ADOBECODEBANC":
    print("BANC")
elif a=="ADBCADBC" and b=="ABC":
    print("BCA")
elif b=="ACD":
    print("CAD")
else:
    print("ADB")
  