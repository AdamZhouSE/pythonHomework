s = input().split()
n = int(s[0])
q = int(s[1])
getOff = []
for i in range(0,q):
    sentence = input().split()
    if(sentence[0] == 'M'):
        x = int(sentence[1])
        a = int(sentence[2])
        getOff.append([x,a])
        getOff.sort(key = lambda x: x[0])
    elif(sentence[0] == 'D'):
        y = int(sentence[1])
        b = int(sentence[2])
        age = list(filter(lambda x: x[0] <= y and x[1] >= b,getOff))
        if(age == []):
            print(-1)
        else:
            age.sort(key = lambda x: x[1])
            print(age[0][1])