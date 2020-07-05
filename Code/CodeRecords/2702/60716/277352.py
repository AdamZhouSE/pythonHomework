strs1 = input()
strs2 = input()
strs3 = input()
strs4 = input()
strs0 = '0000000'
strs5 = '0000000'
strs1 = '0'+strs1+'0'
strs2 = '0'+strs2+'0'
strs3 = '0'+strs3+'0'
strs4 = '0'+strs4+'0'
lists = list()
lists.append(strs0)
lists.append(strs1)
lists.append(strs2)
lists.append(strs3)
lists.append(strs4)
lists.append(strs5)
for i in lists:
    print(i)
index = 0
for i in range(1,len(lists)-1):
    for j in range(1,6):
        if not lists[i][j]==0: 
            temp = list()
            temp.append(lists[i][j-1])
            temp.append(lists[i][j+1])
            temp.append(lists[i-1][j])
            temp.append(lists[i+1][j])
            print("{},{}".format(i,j))
            print(temp)
            if temp.count('0')==3 and temp.count('1')==1:
                print("success")
                index+=1
print(index)