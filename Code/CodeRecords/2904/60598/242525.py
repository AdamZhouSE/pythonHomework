String = input()
num = int(String)
if num < 0:
    String = String[1:][::-1]
else:
    String = String[::-1]
if num !=0:
    String = String.replace("0", "")
if num < 0:
    String = "-"+String
print(String)
