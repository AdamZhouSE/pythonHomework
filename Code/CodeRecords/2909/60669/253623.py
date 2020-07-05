string=input()
maxLetters=int(input())
minSize=int(input())
maxSize=int(input())
record={}

for i in range(0,len(string)-minSize+1):
    temp=string[i:i+minSize]
    charList=[]
    for char in temp:
        if char not in charList:
            charList.append(char)
    if len(charList)<=maxLetters:
        if record.get(temp)==None:
            record[temp]=1
        else:
            record[temp]=record.get(temp)+1
try:
    print(max(record.values()))
except:
    print(0)
