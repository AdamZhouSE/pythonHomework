n = int(input());
list = [int(x) for x in input().split()];
list.sort();
num = list[(int((len(list)-1)/2))];
# if(num==3):
#     print(list);
print(num);