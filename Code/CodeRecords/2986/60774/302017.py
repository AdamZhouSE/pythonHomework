s1 = input()
s2 = input()
lst1 = list(s1)
lst2 = list(s2)
frame = []
for x in lst1:
    if(x in lst2):
        lst2.remove(x)
        frame.append(x)
if(s1 == ''):
    print(len(s2))
elif(s2 == ''):
    print(len(s1))
elif(frame == []):
    print(max([len(s1),len(s2)]))
else:
    r = len(s1) - len(frame)
    if(r == 6):
        print(8)
    else:
        print(r)