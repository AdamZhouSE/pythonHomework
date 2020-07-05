dict_ref = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
num = int(input())
res = ''
first = int(num / 26)
second = num % 26
res = dict_ref[second]
while first > 26:
    second = first % 26
    first = int(first / 26)
    res = dict_ref[second] + res
if first != 0:
    res = dict_ref[first] + res
print(res)