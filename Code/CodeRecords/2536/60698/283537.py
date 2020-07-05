def test():
    tickets=list(eval(input()))
    begin=[]
    for ticket in tickets:
        if ticket[0]=="JFK":
            if begin==[]:
                begin=ticket
            else:
                if ticket[1]<begin[1]:
                    begin=ticket
    if begin==[]:
        return
    else:
        res=[]
        res.append(begin[0])
        res.append(begin[1])
        while True:
            ok=False
            for ticket in tickets:
                if ticket[0]==begin[1]:
                    ok=True
                    begin=ticket
                    res.append(begin[1])
                    tickets.remove(begin)
                    break
            if not ok:
                break
        print(res)


test()