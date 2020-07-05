string = input()
re = string
pattern = input()
temp = string.find(pattern)
while(temp != -1):
    string = string[:temp] + string[temp + len(pattern):]
    temp = string.find(pattern)
if(string == ""):
    print(pattern,end = "")
else:
    print(string,end = "")
