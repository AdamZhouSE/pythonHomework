def check(index:int):
    needs = 0
    for i in lists:
        needs += i//index if i%index==0 else i//index+1
    if needs>H:
        return False
    else:
        return True
lists = list(eval(input()))
H = int(input())
add = 0
for i in lists:
    add+=i
num = add//H if add%H==0 else add//H+1
while True:
    checkFinished = check(num)
    if checkFinished:
        break
    else:
        num+=1
print(num)