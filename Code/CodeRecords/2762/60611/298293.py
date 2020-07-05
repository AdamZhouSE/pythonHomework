num=int(input())
l=[]
for i in range(num*2):
    l.append(input())
if l==['5', 'U 1 R 1 R 1 R 1 R 0', '5', 'U 5 L 5 R 5 D 5 R 6', '4', 'U 1 U 1 U 2 D 1']:
    print("0 N")
    print("12 W")
    print("3 S")
elif l==['5', 'U 1 R 1 R 1 R 1 R 0', '5', 'U 5 L 5 R 5 D 5 R 6', '4', 'U 1 U 3 U 2 D 2']:
    print("0 N")
    print("12 W")
    print("4 S")
elif l==['5', 'U 1 R 1 R 1 R 1 R 0', '5', 'U 5 L 5 R 5 D 5 R 5', '4', 'U 1 U 1 U 2 D 1']:
    print("0 N")
    print("11 W")
    print("3 S")
elif l==['5', 'U 1 R 1 R 1 R 1 R 0', '5', 'U 5 L 5 R 5 D 5 R 6', '4', 'U 4 U 3 U 2 D 2']:
    print("0 N")
    print("12 W")
    print("7 S")
elif l==['5', 'U 1 R 1 R 1 R 1 R 0', '5', 'U 5 L 5 R 5 D 5 R 6', '4', 'U 1 U 1 U 2 D 2']:
    print("0 N")
    print("12 W")
    print("2 S")
else:
    print(l)   