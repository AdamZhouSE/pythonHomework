def makeList(string):
    list=[]
    for i in range(0,26):
        list.append(string.count(chr(i+65)))
    return list
string=input()
number=int(input())
max_number=0
list=makeList(string)
window_length=number+int(max(list))
for i in range(0,len(string)-window_length):
    for j in range(0,26):
        if string[i:i+window_length].count(chr(j+65))>max_number:
            max_number=string[i:i+window_length].count(chr(j+65))
print(max_number)