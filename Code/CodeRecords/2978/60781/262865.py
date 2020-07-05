import re


userInput = input()
info = re.split("\s+",userInput)
data = []

for number in info:
    data+=[number]





print(ord(data[0][0])-ord(data[1][0]))