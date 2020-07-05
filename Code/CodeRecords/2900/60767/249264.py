def numOfChars(title):
    title.replace(" ","")
    return len(title)

title = input()
print(numOfChars(title),end="")