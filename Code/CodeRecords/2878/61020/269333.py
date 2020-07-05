first_line = input()
second_line = input()

n_and_k_list = first_line.split()
n = int(n_and_k_list[0])
k = int(n_and_k_list[1])

a_list = second_line.split()
# result = int(a_list[0])
list_to_be_filtered = []

for i in range(0, len(a_list)):
    if k % (int(a_list[i])) == 0:
        list_to_be_filtered.append(k // int(a_list[i]))

print(min(list_to_be_filtered))
