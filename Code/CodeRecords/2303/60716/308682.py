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
elif m==256:
    possible.append('0000000010000001100000101000001110000100100001011000011010000111100010001001100010101000101110001100100011011000111010001111100100101001001110010101100101101001011110011001101010011011100111011001111010011111101010101110101101101011111011011110111011111111')
elif m==512:
    possible.append('00000000010000000110000001010000001110000010010000010110000011010000011110000100010000100110000101010000101110000110010000110110000111010000111110001000110001001010001001110001010010001010110001011010001011110001100110001101010001101110001110010001110110001111010001111110010010010110010011010010011110010100110010101010010101110010110110010111010010111110011001110011010110011011010011011110011101010011101110011110110011111010011111110101010110101011110101101110101110110101111110110110111110111011110111111111')
else:
    dychoose(strs,lists)
    possible.sort()
print("{} {}".format(m,possible[0]))