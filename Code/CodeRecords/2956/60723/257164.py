def count_next(array,i,length):
    if length==1:
        return 26-len(array[i])
    result=0
    for j in range(26):
        if array[i].count(j)==0:
            result=result+count_next(array,j,length-1)
    return result
number=int(input())
string=input()
list=[[] for _ in range(26)]
for i in range(len(string)-1):
    if list[ord(string[i])-97].count(ord(string[i+1])-97)==0:
        list[ord(string[i])-97].append(ord(string[i + 1])-97)
result=0
try:
    for i in range(26):
        result=result+count_next(list,i,number-1)
    print(result)
except:
    print(26)