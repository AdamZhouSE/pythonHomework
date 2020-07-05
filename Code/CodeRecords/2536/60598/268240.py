import queue
tickets = input()[1:-1]
i = 0
record = dict()
while i < len(tickets):
    if tickets[i] == "[":
        start = i
        while tickets[i] != "]":
            i += 1
        temp = tickets[start + 1:i].split(",")
        From = temp[0].replace("\"","")
        To = temp[1].replace("\"","").replace(" ","")
        if not From in record:
            record[From] = []
            record[From].append(To)
        else:
            record[From].append(To)
            record[From] = sorted(record[From])
    i += 1
q = queue.Queue()
q.put("JFK")
result = []
while not q.empty():
    temp = q.get()
    result.append(temp)
    if temp in record:
        if len(record[temp]) == 0:
            break
        string = record[temp][0]
        q.put(string)
        record[temp].remove(string)
print(result)
