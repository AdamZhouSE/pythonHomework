s = ' '.join(input().split())
strings = s.split(' ')
length = len(s[0])
string = s[0]
for temp_str in strings:
    if(len(temp_str)>length):
        length = len(temp_str)
        string = temp_str
print(string)