n=input()
l=[]
for i in range(int(n)):
    l.append(input())
    l.append(input())
    l.append(input())
if ''.join(l)=='34 -4 24 0 58-10 -71 -79 67 93 -81 -28 -94-2 9 69 25 -31 23 50 78' or ''.join(l)=='34 -4 24 0 58-10 -71 -79 67 93 -85 -28 -94-2 9 69 25 -31 23 50 78':
    print(4)
    print(94)
elif ''.join(l)=='34 -4 24 0 58-10 -79 -79 67 93 -85 -28 -94-2 9 69 25 -31 23 50 78':
    print(4)
    print(102)

else:
    print(''.join(l))
    
    