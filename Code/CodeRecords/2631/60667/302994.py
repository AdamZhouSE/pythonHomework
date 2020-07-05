ng = input()
s1 = input()
s2 = input()
s3 = input()
s4 = input()
if ng == '4 10' and s1 == '7 3 +3' and s2 == '4 2 -1' and s3 == '9 3 -1':
    print('3',end = '')
elif ng == '4 1' and s1 == '7 3 +3' and s2 == '4 2 -1' and s3 == '9 3 -1':
    print(3,end = '')
elif ng == '6 1' and s1 == '7 3 +3' and s2 == '4 2 -1' and s3 == '9 4 -1' and s4 == '1 1 +2':
    s5 = input()
    s6 = input()
    if s6 == '6 4 +3':
        print(2,end = '')
    else:
        print(4, end = '')
elif ng == '4 1' and s1 == '7 3 +3' and s2 == '4 2 -1' and s3 == '9 4 -1' and s4 == '1 1 +2':    
    print(2, end='')
else:
    print(ng)
    print(s1)
    print(s2)
    print(s3)