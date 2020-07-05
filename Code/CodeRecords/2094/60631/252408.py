i = input()
try:
    float(i)
    print('True')
except ValueError:
    print('False')