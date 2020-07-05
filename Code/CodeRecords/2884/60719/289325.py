def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x



def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def handle_each_use_case():
    n = int(input())
    if n % 5 == 0:
        return -1
    return n % 5


limit = to_int_list(input(), " ")
sold = to_int_list(input(), " ")
count = 0
for i in range(0, limit[0]-1):
    for j in range(i+1, limit[0]):
        if abs(sold[i]-sold[j]) <= limit[1]:
            count += 2
print(count)