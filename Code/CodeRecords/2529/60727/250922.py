def so(num):
    for i in range(0,32):
        if ''.join(sorted(str(pow(2,i))))==''.join(num):
            return 'true'
    return 'false'
a=input()
print(so(sorted(a)))
        