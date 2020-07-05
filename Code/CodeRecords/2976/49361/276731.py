import re

lines = []
while True:
    try:
        lines.append(input())
    except:
        break
outputStr = ""
for index in range(1, len(lines)):
    afterStr = re.sub(lines[0].replace(" ", ""), "", lines[index].replace(" ", ""), flags=re.IGNORECASE)
    outputStr += afterStr + "\n"
print(outputStr.strip("\n"))