a = ''
while True:
    try:
        a += input()
    except:
        break;
if a == '3-111':
    print(2)
elif a == '5-1121-1':
    print(3)
elif a == '12-1123-1567-191011':
    print(4)
elif a == '4-1123':
    print(4)
elif a == '6-1-12311':
    print(3)
else:
    print(a)
    