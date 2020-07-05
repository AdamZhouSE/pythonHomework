aStr = input()
if aStr.strip() == "":
    aStr = input()
bStr = input()
str = '123132231213321312==321312213231123132'
if bStr.strip() == "":
    bStr = input()
if len(aStr.strip()) != len(bStr.strip()):
    print(1)
elif aStr.strip() == bStr.strip():
    print(2)
elif aStr.strip().lower() == bStr.strip().lower():
    print(3)
else:
    print(4)