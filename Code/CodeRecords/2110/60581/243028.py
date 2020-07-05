str = int(input())

while str%2==0 :
    str = str/2

while str%5==0 :
    str = str/5

while str%3==0:
    str = str/3

if str==1:
    print(True)
else:
    print(False)