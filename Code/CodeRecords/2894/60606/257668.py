n = int(input())
s = input()
max = s.count("VK")
for i in range(len(s)):
    temp = list(s)
    if temp[i] == "K":
        temp[i] = "V"
    temp2 = "".join(temp).count("VK")
    if temp2 > max:
        max = temp2
for i in range(len(s)):
    temp = list(s)
    if temp[i] == "V":
        temp[i] = "K"
    temp2 = "".join(temp).count("VK")
    if temp2 > max:
        max = temp2
print(max,end="")
