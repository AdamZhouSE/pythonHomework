def check(num):
    i=0
    while True:
        if pow(2,i)>num+1:
            return i-1
        i+=1
init=input()[1:-1].split(',')
judge=True#没有符合要求的null
for i in range(len(init)):
    if init[i]=='null':
        if i%2==1:
            if init[i+1]=='null':
                judge=False
                print(check(i))
                break
if judge:
    print(check(len(init)))