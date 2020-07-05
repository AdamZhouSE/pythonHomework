def check(needs:list(),cap:int):
    indeed = 0
    while len(needs)>0:
        index = 0
        while True:
            if len(needs)==0 or index>cap:
                break
            else:
                index += needs.pop(0)
        indeed+=1
    if indeed>day: return False
    else: return True
lists = list(eval(input()))
day = int(input())
#print(lists)
#print(day)
capbility = max(lists)
while True:
    templist = lists.copy()
    if check(templist,capbility): break
    capbility+=1
print(capbility)