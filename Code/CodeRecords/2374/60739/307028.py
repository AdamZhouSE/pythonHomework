def getDict(list):
    dict = {}
    for key in list:
        dict[key] = dict.get(key, 0) + 1

    l = sorted(dict.items(), key=lambda x:x[1], reverse=True)

    l = bubble_sort(l)
    # print(l)

    out_str = []
    for i in l:
        for j in range(i[1]):
            out_str.append(i[0])

    out_str = " ".join(str(i) for i in (out_str)) + ' '
    return out_str

def bubble_sort(dict):
		for i in range(len(dict)-1):
			for j in range(len(dict)-1-i):
				if dict[j][0] > dict[j+1][0] and dict[j][1] == dict[j+1][1]:
					dict[j], dict[j+1] = dict[j+1],dict[j]
		return dict

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    input()
    l = getInput()
    print(getDict(l))