def letterType(letters,limit):
    letters = set(letters)
    if len(letters)<=limit:
        return True
    else:
        return False
    
String = input()
limitType = int(input())
minSize = int(input())
maxSize = int(input())
count = {}
maxCount = 0
for i in range(len(String)-minSize+1):
    str1 = String[i:i+minSize]
    if letterType(str1,limitType):
        nowCount = count.get(str1,0)
        count[str1] = nowCount + 1
        if count[str1] > maxCount:
            maxCount = count[str1]
print(maxCount)
    