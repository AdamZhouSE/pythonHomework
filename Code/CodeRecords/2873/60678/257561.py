nANDm = input().split()
n = int(nANDm[0])
m = int(nANDm[1])
string = input().replace(' ', '')
numsClicked = input().replace(' ','')
password = []
for i in string:
    if numsClicked.find(i) != -1:
        password .append(i)
print(' '.join(password))