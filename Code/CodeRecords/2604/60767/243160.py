def func(letters,target):
    for i in letters:
        if (i > target):
            return i
    return letters[0]
temp = input()
temp = temp.replace(" ","")
temp = temp.replace(",","")
temp = temp.replace("[","")
temp = temp.replace("]","")
letters = []
for i in range(1,int((len(temp)/3)+1)):
    letters.append(temp[3*i-2])
target = input()
print(func(letters,target))
