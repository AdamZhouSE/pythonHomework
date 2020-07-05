def sum_of_geometric_sequence(a1, n, q):
    return a1 * ((q ** n) - 1) // (q - 1)


num_of_cases = int(input())
case_list = []
for i in range(0, num_of_cases):
    current_input = input()
    case_list.append((int(current_input[0]), int(current_input[2])))

for case in case_list:
    print(sum_of_geometric_sequence(1, case[0], case[1]))
