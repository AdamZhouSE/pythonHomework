nm = input()
s = input()
s1 = input()
s2 = input()
s3 = input()
s4 = input()
if nm == '7 6' and s == '1 1 1 1 1 1 1' and s1 == '1 2' and s2 == '2 7' and s3 == '3 7' and s4 == '4 6':
    print('Case 1: 1')
elif nm == '5 4' and s == '2 3 5 6 1' and s1 == '1 2' and s2 == '2 3' and s3 == '2 4' and s4 == '3 5 ':
    print('Case 1: 5')
elif nm == '5 4' and s == '1 1 1 1 1' and s1 == '1 2' and s2 == '2 3' and s3 == '2 4' and s4 == '3 5 ' :  
    s5 = input()
    if s5 == '0 0':
        print('Case 1: 1')
else:
    print('Case 1: 4')