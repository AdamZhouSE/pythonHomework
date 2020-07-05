a=input()
b=input()
if len(a)!=len(b):
    print("1")
elif a==b:
    print("2")
elif a.upper()==b.upper():
    print("3")
else:print("4")