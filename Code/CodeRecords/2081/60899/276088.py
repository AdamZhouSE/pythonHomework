strOfA = input()
strOfB = input()
count = 0
temp = strOfA
while True:
    if len(temp) < len(strOfB):
        break
    if temp.find(strOfB)!=-1:
        count+=1
        temp = temp[temp.find(strOfB)+1:]
        #temp = temp[temp.find(strOfB[0]):]
    else:break
print(count,end="")
