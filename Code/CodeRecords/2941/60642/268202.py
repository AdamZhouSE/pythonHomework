num = int(input())
instr = input()
dictionary = ['F','D','C','B','A']
sum = 0
for i in range(len(instr)):
    sum = sum+dictionary.index(instr[i])
print(sum/num)