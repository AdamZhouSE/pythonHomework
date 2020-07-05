def getMax(list):
    dict = {}
    for key in list:
        dict[key] = dict.get(key, 0) + 1
    
    m = max(dict, key=dict.get)
    print(dict[m])
    return dict

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

input()
l = getInput()
getMax(l)
