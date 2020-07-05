string=input()
nums=[]
for i in range(len(string)):
    for j in range(len(string)):
        if i<j:
            nums.append(int(string[:i]+string[j]+string[i+1:j]+string[i]+string[j+1:]))
        elif i>j:
            nums.append(int(string[:j]+string[i]+string[j+1:i]+string[j]+string[i+1:]))
        else:
            nums.append(int(string))
print(max(nums))