record = []
for i in range(0,21):
    record.append(pow(4,i))
if(int(input()) in record):
    print('true')
else:
    print('false')