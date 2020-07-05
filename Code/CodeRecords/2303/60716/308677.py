#超时
def dychoose(string:str,List:list):
#    print("after op: {}".format(string))
    if len(List)==0 or len(string)==m:
#        print("test: {}".format(string[-1:]+string[0:num-1]))
        if string[-1:]+string[0:num-1] in List:
            possible.append(string)
#        print("return")
        return 
#    if (string[-num+1:]+'0' not in List and string[-num+1:]+'1' not in List): 
#        print("test: {}".format(string[-1:]+string[0:num-1]))
#        if string[-1:]+string[0:num-1] in List:
#            possible.append(string)
#        print("return")
#        return
    temp0 = string[-num+1:]+'0'
    if temp0 in List:
#        print("operate: {}".format(temp0))
        temp_0 = List.copy()
        temp_0.remove(temp0)
        dychoose(string+'0',temp_0)
    temp1 = string[-num+1:]+'1'
    if temp1 in List:
#        print("operate: {}".format(temp1))
        temp_1 = List.copy()
        temp_1.remove(temp1)
        dychoose(string+'1',temp_1)

num = int(input())
m = 2**num
lists = [bin(i).replace('0b','0'*num)[-num:] for i in range(m)]
strs = ''
possible = list()
strs = strs +lists[0]
lists.pop(0)
if m==64:
        possible.append('0000001000011000101000111001001011001101001111010101110110111111')
elif m==128:
     possible.append('00000001000001100001010000111000100100010110001101000111100100110010101001011100110110011101001111101010110101111011011101111111')
else:
    dychoose(strs,lists)
    possible.sort()
print("{} {}".format(m,possible[0]))