def numOfChars(title):
    title = title.replace(" ","")
    title = title.replace("/n","")
    return len(title)

title = input()
print(numOfChars(title),end="")