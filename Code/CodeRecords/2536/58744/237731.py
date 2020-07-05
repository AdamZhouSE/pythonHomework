tickets_list = list(eval(input()))
tickets_dict = dict()
sorted_tickets = list()

list_len = len(tickets_list)
cur_pos = 0

while cur_pos < list_len:
    cur_from = tickets_list[0][0]
    cur_to = list()
    index = 0

    for j in range(len(tickets_list)):
        if tickets_list[index][0] == cur_from:
            cur_to.append(tickets_list[index][1])
            tickets_list.remove(tickets_list[index])
            cur_pos += 1
        else:
            index += 1
    
    tickets_dict[cur_from] = sorted(cur_to)

stack = list()

def dfs(src):
    if src in tickets_dict:
        dest = tickets_dict[src][0]
        tickets_dict[src].remove(dest)
        if len(tickets_dict[src]) == 0:
            tickets_dict.pop(src)
        dfs(dest)
        dfs(src)
    else:
        stack.append(src)

dfs('JFK')
sorted_tickets = list(reversed(stack))[:]

print(sorted_tickets)
