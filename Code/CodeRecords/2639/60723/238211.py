def makeList(string):
    list=[]
    for i in range(0,26):
        list.append(string.count(chr(i+65)))
    return list
string=input()
number=int(input())
max_number=0
list=makeList(string)
window_length=number+max(int(max(list)),len(string))
if window_length>=len(string):
    print(len(string))
else:
    for i in range(0,len(string)-window_length):
        for j in range(0,26):
            if string[i:i+window_length].count(chr(j+65))>max_number:
                max_number=string[i:i+window_length].count(chr(j+65))
    print(max_number+number)