a = input()
b = input()
if len(a) != len(b):
    print(1)
    quit()
if a == b:
    print(2)
    quit()
if a.lower() == b.lower():
    print(3)
else:
    print(4)
    