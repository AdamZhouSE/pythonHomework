s=input("")
result = 0 
for letter in s:
    result = result * 26 + ord(letter) - ord('A') + 1
print(result)